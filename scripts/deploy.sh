#!/usr/bin/env bash
# Rebuild locally (sanity check), commit, and push. Cloudflare Pages builds main on push.
set -euo pipefail
cd "$(dirname "$0")/.."
npm run build >/dev/null
git add -A
git diff --cached --quiet && { echo "nothing new to deploy"; exit 0; }
git commit -qm "Refresh: $(python3 -c 'import json;d=json.load(open("src/data/usecases.json"));print(len(d["usecases"]),"use cases,",len(d["templates"]),"templates, scan",d["meta"]["lastScan"])')"
git push -q origin main
echo "pushed; Cloudflare Pages will publish https://grok-bot-showcase.pages.dev in ~1 min"
