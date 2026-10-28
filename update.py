#!/usr/bin/env python3
"""Agrega nuevas sugerencias, conserva las del día anterior y BORRA las de más de 48 h (2 días) junto con su imagen. Actualiza meta.generated_at.
Uso: python3 update.py [nuevas.json]  (nuevas.json = lista de entradas a agregar)"""
import json,sys,os,datetime as dt
now=dt.datetime.now(dt.timezone.utc);cut=now-dt.timedelta(hours=48)
S=json.load(open('data/suggestions.json'))
if len(sys.argv)>1:
    ids={e['id'] for e in S['entries']};S['entries']+= [e for e in json.load(open(sys.argv[1])) if e['id'] not in ids]
p=lambda e:dt.datetime.fromisoformat(e['detected_at'].replace('Z','+00:00'))
old=[e for e in S['entries'] if p(e)<cut]
keep_imgs={e.get('image') for e in S['entries'] if p(e)>=cut}
for e in old:
    i=e.get('image')
    if i and i not in keep_imgs and os.path.exists(i): os.remove(i)
S['entries']=[e for e in S['entries'] if p(e)>=cut]
S['meta']['generated_at']=now.strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(S,open('data/suggestions.json','w'),ensure_ascii=False,indent=1)
print(len(S['entries']),'vigentes,',len(old),'borradas (>48 h)')
