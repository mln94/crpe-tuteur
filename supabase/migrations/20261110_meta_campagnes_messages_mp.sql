alter table public.meta_campagnes add column if not exists messages_mp jsonb;
comment on column public.meta_campagnes.messages_mp is 'Messages privés à envoyer aux personnes qui répondent : [{titre, quand, texte}]';
