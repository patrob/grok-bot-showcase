#!/usr/bin/env python3
"""Append X search-result dumps (files from the x MCP) to raw/replies.jsonl, deduped by id.
Usage: ingest.py FILE [FILE...]  -> prints next_token of the last file and new posts."""
import json,sys,os
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out=os.path.join(root,'raw','replies.jsonl')
seen=set()
if os.path.exists(out):
    for l in open(out): seen.add(json.loads(l)['id'])
nt=None
with open(out,'a') as f:
    for fn in sys.argv[1:]:
        s=open(fn).read(); i=s.find('{'); 
        d,_=json.JSONDecoder().raw_decode(s[i:])
        u={x['id']:x['username'] for x in d.get('includes',{}).get('users',[])}
        nt=d.get('meta',{}).get('next_token')
        for p in d.get('data',[]):
            if p['id'] in seen: continue
            seen.add(p['id'])
            t=(p.get('note_tweet') or {}).get('text') or p['text']
            r={'id':p['id'],'handle':u.get(p['author_id'],'?'),'created_at':p.get('created_at'),'likes':p.get('public_metrics',{}).get('like_count',0),'text':t}
            f.write(json.dumps(r,ensure_ascii=False)+'\n')
            if len(t)>60: print('---',r['id'],'@'+r['handle'],r['likes'],'|',t.replace('\n',' / '))
print('NEXT',nt, 'total',len(seen))
