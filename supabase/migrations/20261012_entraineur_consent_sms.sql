-- Entraîneur CRPE : accord facultatif pour être contacté par WhatsApp ou SMS (offres, contenus, retour sur la préparation).
-- Ajout seul, rien n'est modifié ni supprimé.
alter table public.entraineur_leads add column if not exists consent_contact_sms boolean not null default false;
