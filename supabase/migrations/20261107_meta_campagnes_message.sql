-- Suivi des publications Meta : message (texte du post) enregistré une fois pour toute la campagne.
alter table public.meta_campagnes add column if not exists message text, add column if not exists message_maj_at timestamptz;
