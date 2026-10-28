#!/usr/bin/env python3
"""Mueve a data/archive.json las sugerencias con más de 72 h (y sus imágenes a assets/img/archive/) y actualiza meta.generated_at.
Uso: python3 update.py [nuevas.json]  (nuevas.json = lista de entradas a agregar)"""
import json,sys,os,shutil,datetime as dt
now=dt.datetime.now(dt.timezone.utc);cut=now-dt.timedelta(hours=72)
S=json.load(open('data/suggestions.json'));A=json.load(open('data/archive.json'))
if len(sys.argv)>1:
    ids={e['id'] for e in S['entries']};S['entries']+= [e for e in json.load(open(sys.argv[1])) if e['id'] not in ids]
p=lambda e:dt.datetime.fromisoformat(e['detected_at'].replace('Z','+00:00'))
old=[e for e in S['entries'] if p(e)<cut]
os.makedirs('assets/img/archive',exist_ok=True)
for e in old:
    i=e.get('image')
    if i and os.path.exists(i) and '/archive/' not in i:
        d='assets/img/archive/'+os.path.basename(i);shutil.move(i,d);e['image']=d
A['entries']+=old;S['entries']=[e for e in S['entries'] if p(e)>=cut]
S['meta']['generated_at']=now.strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(S,open('data/suggestions.json','w'),ensure_ascii=False,indent=1);json.dump(A,open('data/archive.json','w'),ensure_ascii=False,indent=1)
print(len(S['entries']),'vigentes,',len(A['entries']),'archivadas')
