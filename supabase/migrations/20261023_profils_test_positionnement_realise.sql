-- profils_utilisateurs.test_positionnement_fait devient test_positionnement_realise (même nom que dans quiz_comptes et Klaviyo) :
-- false à l'inscription (valeur par défaut), passé à true par le déclencheur on_quiz_compte_change quand le test est enregistré.
alter table public.profils_utilisateurs rename column test_positionnement_fait to test_positionnement_realise;
alter table public.profils_utilisateurs alter column test_positionnement_realise set default false;

create or replace function public.sync_profil_depuis_quiz()
 returns trigger
 language plpgsql
 security definer
 set search_path to 'public'
as $function$
begin
  insert into public.profils_utilisateurs (user_id, test_positionnement_realise, test_positionnement_at, note_positionnement, reponses_positionnement,
                                           lien_rapport_positionnement, lien_rapport_expire_at)
  values (new.user_id, new.positionnement_at is not null, new.positionnement_at, new.note_positionnement, new.reponses_positionnement,
          new.lien_rapport, new.rapport_expire_at)
  on conflict (user_id) do update set
    test_positionnement_realise = excluded.test_positionnement_realise,
    test_positionnement_at      = excluded.test_positionnement_at,
    note_positionnement         = excluded.note_positionnement,
    reponses_positionnement     = excluded.reponses_positionnement,
    lien_rapport_positionnement = excluded.lien_rapport_positionnement,
    lien_rapport_expire_at      = excluded.lien_rapport_expire_at;
  return new;
end;
$function$;

-- Remise à niveau des profils existants à partir des tests enregistrés
update public.profils_utilisateurs p
set test_positionnement_realise = exists (select 1 from public.quiz_comptes q where q.user_id = p.user_id and q.positionnement is not null);
