#!/usr/bin/env python3
"""REEMPLAZA TODO en cada corrida: borra todas las sugerencias anteriores de data/suggestions.json
y sus imágenes en assets/img/, y deja solo el set nuevo. Actualiza meta.generated_at.
Uso: python3 update.py nuevas.json  (lista de entradas nuevas; sus imágenes ya deben existir en assets/img/)"""
import json,sys,os,glob,datetime as dt
if len(sys.argv)<2: sys.exit('uso: python3 update.py nuevas.json')
N=json.load(open(sys.argv[1]));now=dt.datetime.now(dt.timezone.utc)
for e in N:
    assert e.get('image') and os.path.exists(e['image']),f"falta imagen: {e.get('id')}"
keep={os.path.normpath(e['image']) for e in N}
S=json.load(open('data/suggestions.json'));old=len(S.get('entries',[]))
gone=[p for p in glob.glob('assets/img/**/*.*',recursive=True) if os.path.normpath(p) not in keep]
for p in gone: os.remove(p)
S={'meta':{'generated_at':now.strftime('%Y-%m-%dT%H:%M:%SZ'),'note':'Set completo nuevo; las sugerencias anteriores se borraron.'},'entries':N}
json.dump(S,open('data/suggestions.json','w'),ensure_ascii=False,indent=1)
print(len(N),'nuevas,',old,'anteriores borradas,',len(gone),'imágenes borradas')
