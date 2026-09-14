'use strict';
const fs=require('fs'), path=require('path');
const dir=path.resolve(__dirname,'../notizen');
const files=fs.readdirSync(dir).filter(x=>/^20\d\d-(herbst|fruehjahr)\.md$/.test(x)).sort();
let total=0, report=[];
for(const file of files){
 const s=fs.readFileSync(path.join(dir,file),'utf8');
 const headings=[...s.matchAll(/^###\s+(\d+\.\d+)\s*\|\s*([^|]+)\|\s*(\d+|\?)\s*P\s*\|\s*([^|]+)\|\s*([ab]\d+)\s*$/gm)];
 const issues=[],points={},seen=new Set();
 for(let i=0;i<headings.length;i++){
  const h=headings[i], main=h[1].split('.')[0], block=s.slice(h.index,headings[i+1]?.index??s.length);
  if(seen.has(h[1]))issues.push('Doppelte Nummer '+h[1]);seen.add(h[1]);
  if(!['Rechnen','Zeichnen','Erklären','Nennen','Zuordnen','Fachtext'].includes(h[4].trim()))issues.push('Unbekannter Typ '+h[4]);
  if(!/^(a[1-9]|b(?:[1-9]|10|11))$/.test(h[5]))issues.push('Kapitel '+h[5]);
  if(!/Aufgabe\s*(?:\(|:)/.test(block))issues.push(h[1]+' Aufgabe fehlt');
  if(!/Material/.test(block))issues.push(h[1]+' Material fehlt');
  if(!/Lösungskern/.test(block))issues.push(h[1]+' Lösungskern fehlt');
  if(!/Bemerkung/.test(block))issues.push(h[1]+' Bemerkung fehlt');
  if(!/Heftbezeichnung/.test(block))issues.push(h[1]+' Heftbezeichnung fehlt');
  points[main]=(points[main]||0)+Number(h[3]);
 }
 const sum=Object.values(points).reduce((a,b)=>a+b,0); total+=sum;
 report.push({file,subtasks:headings.length,points,sum,issues});
}
const output={date:new Date().toISOString().slice(0,10),examCount:files.length,subtasks:report.reduce((n,r)=>n+r.subtasks,0),points:total,exams:report};
fs.writeFileSync(path.join(dir,'PRUEF-EXTRAKTIONEN.json'),JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify(output,null,2));

