"""Root speichert vorgeschlagene Dateiinhalte aus eigenen, nur lesenden Unteragenten."""
import argparse, json, pathlib, hashlib, re
parser=argparse.ArgumentParser()
parser.add_argument('agent')
parser.add_argument('--allow',nargs='+',required=True)
parser.add_argument('--apply',action='store_true')
a=parser.parse_args()
base=pathlib.Path(r'C:\Users\mu.aycetin\Desktop\Lernen\bau').resolve()
parent='01a0660b-9ad4-7812-93e0-aa4a8f1d0e02'
logs=pathlib.Path(r'C:\Users\mu.aycetin\.codex\sessions\2026\09\03')
statefile=base/'notizen/AGENTEN-UEBERNAHMEN.json'
state=json.loads(statefile.read_text(encoding='utf-8')) if statefile.exists() else []
seen={x['bundle'] for x in state}
matched=[]
for log in logs.glob('*.jsonl'):
 with log.open(encoding='utf-8') as stream:
  meta=json.loads(stream.readline()).get('payload',{})
  if meta.get('parent_thread_id')!=parent or meta.get('agent_path')!=a.agent: continue
  for line in stream:
   try: rec=json.loads(line)
   except json.JSONDecodeError: continue
   p=rec.get('payload',{})
   if rec.get('type')=='response_item' and p.get('type')=='message' and p.get('role')=='assistant':
    finaltext='\n'.join(x.get('text','') for x in p.get('content',[]))
    pairs=re.findall(r'`bau/([^`]+)`[^\n]*\n\n```(?:markdown|text)\n(.*?)\n```',finaltext,re.S)
    if pairs:
     p={'type':'custom_tool_call_output','call_id':p.get('id'),'output':[{'text':'AP1_BUNDLE_V1:'+json.dumps({'files':[{'path':n,'content':v+'\n'} for n,v in pairs]})}]}
   if rec.get('type')!='response_item' or p.get('type') not in ('custom_tool_call_output','function_call_output'): continue
   output=p.get('output',[])
   blocks=output if isinstance(output,list) else [{'text':output}]
   for i,block in enumerate(blocks):
    val=block.get('text','')
    prefix='AP1_BUNDLE_V1:'
    if not val.startswith(prefix):continue
    ident=log.name+':'+str(p.get('call_id'))+':'+str(i)
    if ident in seen:continue
    bundle=json.loads(val[len(prefix):])
    for item in bundle['files']:
     rel=item['path'].replace('\\','/')
     if rel not in a.allow:raise ValueError('Nicht angeforderter Zielpfad: '+rel)
     target=(base/rel).resolve()
     if not target.is_relative_to(base):raise ValueError('Ziel ausserhalb bau')
     if item.get('mode','write') not in ('write','append'):raise ValueError('Unbekannter Modus')
     content=item['content']
     if not isinstance(content,str):raise ValueError('Inhalt muss Text sein')
     matched.append((ident,rel,len(content),hashlib.sha256(content.encode()).hexdigest()))
     if a.apply:
      target.parent.mkdir(exist_ok=True,parents=True)
      with target.open('a' if item.get('mode')=='append' else 'w',encoding='utf-8',newline='') as out:out.write(content)
    if a.apply:
     state.append({'bundle':ident,'agent':a.agent,'files':[x['path'] for x in bundle['files']]})
     seen.add(ident)
if a.apply:statefile.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for ident,rel,count,digest in matched:print(rel,count,digest)
print('Applied' if a.apply else 'Reviewed',len(matched),'file payloads')

