#!/bin/zsh
# Exécuteur des agents IA du Mac, lancé toutes les 2 minutes par launchd (fr.passcrpe.agents-poller).
#  1. envoie au dashboard /suivi-agents l'état de l'agent blog (articles + Publieur) ;
#  2. à partir de 9h30 (heure de Paris), prévoit le passage de veille des posts d'hier s'il n'existe pas encore ;
#  3. exécute les passages de veille Facebook en attente (celui du jour ou ceux demandés depuis le dashboard).
# Lancé via ~/.passcrpe/PassCRPE Agents.app : une application a le droit de lire le Bureau (protection macOS), pas un script.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
cd /Users/necib/Desktop/DEV/NEW_120426/CRPE || exit 1
LOCK="$HOME/.passcrpe/verrou-agents"
mkdir "$LOCK" 2>/dev/null || {
  # verrou de plus de 3 h = passage planté : on le libère
  [[ -n $(find "$LOCK" -maxdepth 0 -mmin +180 2>/dev/null) ]] && rmdir "$LOCK" && mkdir "$LOCK" || exit 0
}
trap 'rmdir "$LOCK" 2>/dev/null' EXIT
mkdir -p logs/veille-facebook

node scripts/agents_suivi.mjs --sync-blog >/dev/null 2>&1
node scripts/agents_suivi.mjs --etat publieur_launchd "$(launchctl print gui/$(id -u)/fr.passcrpe.publier-articles 2>&1 | grep -E '^\s*(state|runs|last exit code) =' | sed 's/^[[:space:]]*//')" >/dev/null 2>&1

[[ $(TZ=Europe/Paris date +%H%M) -ge 0930 ]] && node scripts/agents_suivi.mjs --planifier-veille >/dev/null 2>&1

while true; do
  read RUN JOUR <<< "$(node scripts/agents_suivi.mjs --prochaine-veille 2>/dev/null)"
  [[ -z "$RUN" ]] && break
  LOG="logs/veille-facebook/run-$JOUR-$(date +%H%M%S).log"
  echo "$(date '+%F %T') passage $RUN pour le $JOUR" >> logs/veille-facebook/poller.log
  open -ga "Google Chrome"; sleep 15
  claude -p "/veille-facebook jour=$JOUR run=$RUN" --chrome \
    --allowedTools "Read" "Write" "Edit" "Bash(mkdir:*)" "Bash(date:*)" "Bash(node scripts/agents_suivi.mjs:*)" "Skill" "ToolSearch" \
    "mcp__claude-in-chrome" "mcp__claude_ai_Google_Sheets" \
    >> "$LOG" 2>&1
  # si l'agent n'a pas enregistré son passage, il est marqué en erreur avec la fin du journal
  node scripts/agents_suivi.mjs --echec-veille "$RUN" "L'agent s'est arrêté sans enregistrer son passage. Fin du journal :
$(tail -c 1500 "$LOG")" >/dev/null 2>&1
done
