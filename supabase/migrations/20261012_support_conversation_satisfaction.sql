-- Support : conversation entre le candidat et l'admin, clôture par le candidat et note de satisfaction.
-- Le premier message reste dans support_tickets.message ; les échanges suivants vont dans support_messages.

-- 1. Messages de la conversation
create table if not exists public.support_messages (
  id         uuid primary key default gen_random_uuid(),
  ticket_id  uuid not null references public.support_tickets(id) on delete cascade,
  author     text not null check (author in ('user', 'admin')),
  body       text not null check (length(btrim(body)) > 0),
  created_at timestamptz not null default now()
);
create index if not exists support_messages_ticket_idx on public.support_messages (ticket_id, created_at);

alter table public.support_messages enable row level security;

create policy "Users view own ticket messages" on public.support_messages
  for select using (exists (select 1 from public.support_tickets t where t.id = ticket_id and t.user_id = auth.uid()));
create policy "Admin view all messages" on public.support_messages
  for select using ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com');
create policy "Admin insert messages" on public.support_messages
  for insert with check ((auth.jwt() ->> 'email') = 'mohamed.necib94310@gmail.com' and author = 'admin');
-- Les candidats écrivent uniquement via support_user_reply (contrôle du propriétaire et du statut)

-- 2. Clôture et satisfaction
alter table public.support_tickets
  add column if not exists closed_at    timestamptz,
  add column if not exists closed_by    text check (closed_by in ('user', 'admin')),
  add column if not exists satisfaction smallint check (satisfaction between 1 and 5),
  add column if not exists rated_at     timestamptz;

-- 3. Reprise des réponses déjà envoyées dans la conversation
insert into public.support_messages (ticket_id, author, body, created_at)
select t.id, 'admin', t.admin_reply, coalesce(t.admin_replied_at, t.created_at, now())
from public.support_tickets t
where t.admin_reply is not null
  and not exists (select 1 from public.support_messages m where m.ticket_id = t.id);

-- 4. Actions du candidat (security definer : il ne peut modifier que ces champs, et seulement sur ses demandes)

-- Répondre : la demande repasse « En attente »
create or replace function public.support_user_reply(p_ticket uuid, p_body text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if p_body is null or length(btrim(p_body)) = 0 then raise exception 'Message vide'; end if;
  if not exists (select 1 from support_tickets where id = p_ticket and user_id = auth.uid() and status <> 'closed') then
    raise exception 'Demande introuvable ou clôturée';
  end if;
  insert into support_messages (ticket_id, author, body) values (p_ticket, 'user', btrim(p_body));
  update support_tickets set status = 'open' where id = p_ticket;
end $$;

-- Clôturer avec une note (possible dès qu'une réponse a été apportée) ;
-- si l'admin a déjà clôturé, permet seulement d'ajouter la note manquante
create or replace function public.support_user_close(p_ticket uuid, p_satisfaction int)
returns void language plpgsql security definer set search_path = public as $$
declare t support_tickets;
begin
  if p_satisfaction is null or p_satisfaction not between 1 and 5 then raise exception 'Note invalide'; end if;
  select * into t from support_tickets where id = p_ticket and user_id = auth.uid();
  if not found then raise exception 'Demande introuvable'; end if;
  if t.satisfaction is not null then raise exception 'Demande déjà notée'; end if;
  if not exists (select 1 from support_messages where ticket_id = p_ticket and author = 'admin') then
    raise exception 'Aucune réponse pour le moment';
  end if;
  update support_tickets set
    status       = 'closed',
    closed_at    = coalesce(closed_at, now()),
    closed_by    = coalesce(closed_by, 'user'),
    satisfaction = p_satisfaction,
    rated_at     = now(),
    user_seen_reply = true
  where id = p_ticket;
end $$;

-- Marquer les réponses comme lues (fait disparaître la pastille de l'onglet Support)
create or replace function public.support_mark_seen()
returns void language sql security definer set search_path = public as $$
  update support_tickets set user_seen_reply = true where user_id = auth.uid() and user_seen_reply = false;
$$;

revoke all on function public.support_user_reply(uuid, text), public.support_user_close(uuid, int), public.support_mark_seen() from public, anon;
grant execute on function public.support_user_reply(uuid, text), public.support_user_close(uuid, int), public.support_mark_seen() to authenticated;
