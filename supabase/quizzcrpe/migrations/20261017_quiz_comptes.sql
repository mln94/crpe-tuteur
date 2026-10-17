-- Projet « quizzcrpe » : comptes du Quiz CRPE (test de positionnement et paiement).
-- Lecture et écriture réservées au serveur : RLS sans politique, fonctions protégées par la clé serveur
-- (QUIZ_SERVER_SECRET, dont seule l'empreinte SHA-256 est stockée ici).

create table if not exists public.quiz_comptes (
  user_id uuid primary key references auth.users (id) on delete cascade,
  email text,
  positionnement jsonb,
  positionnement_at timestamptz,
  paid boolean not null default false,
  paid_at timestamptz,
  paypal_ref text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
alter table public.quiz_comptes enable row level security;

create or replace function public.quiz_cle_ok(p_cle text)
returns boolean language sql immutable set search_path = public, extensions as $$
  select encode(extensions.digest(coalesce(p_cle, ''), 'sha256'), 'hex') = 'e15d6cbade1cb56545823d343e6d74aab29c71fa931cca1bdae97cb74235396b';
$$;

-- État du compte (null si aucune ligne)
create or replace function public.quiz_compte(p_cle text, p_user uuid)
returns table (email text, positionnement jsonb, positionnement_at timestamptz, paid boolean, paid_at timestamptz)
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.quiz_cle_ok(p_cle) then raise exception 'refusé'; end if;
  return query select c.email, c.positionnement, c.positionnement_at, c.paid, c.paid_at from public.quiz_comptes c where c.user_id = p_user;
end $$;

-- Résultat du test de positionnement (enregistré une seule fois)
create or replace function public.quiz_enregistrer_positionnement(p_cle text, p_user uuid, p_email text, p_resultat jsonb)
returns jsonb language plpgsql security definer set search_path = public as $$
declare r jsonb;
begin
  if not public.quiz_cle_ok(p_cle) then raise exception 'refusé'; end if;
  insert into public.quiz_comptes (user_id, email, positionnement, positionnement_at)
  values (p_user, p_email, p_resultat, now())
  on conflict (user_id) do update
    set positionnement = coalesce(public.quiz_comptes.positionnement, excluded.positionnement),
        positionnement_at = coalesce(public.quiz_comptes.positionnement_at, excluded.positionnement_at),
        email = coalesce(excluded.email, public.quiz_comptes.email),
        updated_at = now()
  returning positionnement into r;
  return r;
end $$;

-- Paiement confirmé (PayPal) : renvoie true si le compte vient d'être débloqué, false s'il l'était déjà
create or replace function public.quiz_marquer_paye(p_cle text, p_user uuid, p_ref text)
returns boolean language plpgsql security definer set search_path = public as $$
declare deja boolean;
begin
  if not public.quiz_cle_ok(p_cle) then raise exception 'refusé'; end if;
  select paid into deja from public.quiz_comptes where user_id = p_user;
  insert into public.quiz_comptes (user_id, paid, paid_at, paypal_ref)
  values (p_user, true, now(), p_ref)
  on conflict (user_id) do update
    set paid = true, paid_at = coalesce(public.quiz_comptes.paid_at, now()),
        paypal_ref = coalesce(public.quiz_comptes.paypal_ref, excluded.paypal_ref), updated_at = now();
  return not coalesce(deja, false);
end $$;

revoke all on function public.quiz_cle_ok(text) from public, anon, authenticated;
revoke all on function public.quiz_compte(text, uuid) from public;
revoke all on function public.quiz_enregistrer_positionnement(text, uuid, text, jsonb) from public;
revoke all on function public.quiz_marquer_paye(text, uuid, text) from public;
grant execute on function public.quiz_compte(text, uuid) to anon, service_role;
grant execute on function public.quiz_enregistrer_positionnement(text, uuid, text, jsonb) to anon, service_role;
grant execute on function public.quiz_marquer_paye(text, uuid, text) to anon, service_role;
