-- « Mes notions » : nombre de questions déjà vues par notion (un rond par question faite : bleu si juste, orange si fausse)
drop function if exists public.quiz_notions_liste(text, text);
create function public.quiz_notions_liste(p_matiere text, p_theme text)
returns table (notion text, intitule text, exemple text, classe text, niveau text, nb_questions integer, ordre integer,
               bonnes integer, vues integer, fois integer, statut text, derniere_ok boolean, derniere_at timestamptz)
language sql
stable
security definer
set search_path = public
as $$
  select n.notion, n.intitule, n.exemple, n.classe, n.niveau, n.nb_questions, n.ordre,
         coalesce(cardinality(p.ok), 0), coalesce(cardinality(p.vus), 0), coalesce(p.fois, 0), quiz_statut_notion(p), p.derniere_ok, p.derniere_at
    from quiz_notions n
    left join quiz_progres_notions p on p.user_id = auth.uid() and p.matiere = n.matiere and p.notion = n.notion
   where n.matiere = p_matiere and n.theme = p_theme and auth.uid() is not null
   order by n.ordre
$$;
revoke all on function public.quiz_notions_liste(text, text) from public, anon;
grant execute on function public.quiz_notions_liste(text, text) to authenticated;
