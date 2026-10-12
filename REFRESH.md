# Daily refresh

Source thread: https://x.com/poteto/status/2108808972954423578
Request: https://x.com/onpardev/status/2109460986922959074 (revisit once a day for 2 days: Oct 12 and Oct 13, 2026)

Live: https://grok-bot-showcase.pages.dev
Repo: https://github.com/patrob/grok-bot-showcase (public). Cloudflare Pages project `grok-bot-showcase` builds `main` on every push (`npm run build` -> `dist`, NODE_VERSION 22). Free plan, no custom domain.

## 1. Scan new replies (agent, x MCP namespace; read only, never post)

Only fetch replies newer than the last one already stored:

```
newest=$(python3 -c "import json;print(max(int(json.loads(l)['id']) for l in open('raw/replies.jsonl')))")
```

Call `x.search_posts_all` with
- query: `conversation_id:2108808972954423578 -is:retweet -from:bot -"read this" -"suggest ideas"`
- `since_id`: $newest, `max_results`: 25, `write_to_file`: true
- `post.fields`: `author_id,created_at,public_metrics,text,note_tweet`, `expansions`: `author_id`, `user.fields`: `username`

Repeat with `next_token` until it is absent. Ingest each dump (dedupes by id, prints the substantive new posts):

```
python3 scripts/ingest.py /workspace/agent-tools/<file>.txt [...]
```

For picks whose text looks cut off, or that have links, call `x.get_posts_by_ids` with `post.fields=...,note_tweet,entities` and merge them into `raw/full.json` (same shape as existing entries: handle, likes, text with t.co expanded, urls).

## 2. Add entries

Append tuples to `E_` (use cases) or `T` (templates, real `x.ai/bot/...` share links only) in `scripts/seed.py`, then:

```
python3 scripts/seed.py
```

Rules the seed script enforces or you must follow:
- Every `quote` must be a verbatim substring of the post (script asserts this). Summaries are paraphrase only; invent nothing.
- Credit the poster's @handle and link the post (generated automatically).
- Sections: `value`, `joy`, `quirky`, `workflow`.
- Call it Grok Bot. Don't name any underlying model.
- Bump `lastScan` in seed.py's `meta`; the replies count updates itself.

## 3. Deploy (one command)

```
./scripts/deploy.sh
```

Builds, commits, and pushes; Pages publishes in about a minute.
