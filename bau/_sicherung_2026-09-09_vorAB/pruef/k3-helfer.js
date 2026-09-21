'use strict';
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const sources=new Map();
for(const f of ['QUELLEN-A.md','QUELLEN-B.md'])for(const l of fs.readFileSync(path.join(root,'notizen',f),'utf8').split('\n')){if(!l.startsWith('|'))continue;const c=l.split('|').slice(1,-1).map(s=>s.trim());if(c.length===8&&!sources.has(c[0]))sources.set(c[0],c);}
function chapter(id,title){const used=new Map();let figure=0;
 const q=(key,where)=>{if(!sources.has(key))throw Error('Quelle fehlt: '+key);if(!used.has(key))used.set(key,used.size+1);const n=used.get(key);return `<sup class="q"><a href="#${id}-q${n}" title="${esc(where||sources.get(key)[7])}">${n}</a></sup>`;};
 const p=(s,key,where)=>`<p>${s}${key?q(key,where):''}</p>\n`;
 const card=(slug,name,def,practice,memory,exam,key,where)=>`<dl class="begriff" id="${id}-begriff-${slug}"><dt>${name}</dt>${[def+q(key,where),practice,memory,exam].map((t,i)=>`<dd><span class="label">${['Theorie','Praxis','Merkhilfe und Verwechslung','In der Prüfung'][i]}</span><p>${t}</p></dd>`).join('\n')}</dl>\n`;
 const fig=(title,body,height,caption)=>{figure++;return `<figure class="abb"><svg viewBox="0 0 640 ${height}" role="img" aria-labelledby="${id}-abb${figure}-t"><title id="${id}-abb${figure}-t">${esc(title)}</title>${body}</svg><figcaption>Abb. ${id.toUpperCase()}-${figure}: ${caption}</figcaption></figure>\n`;};
 const table=(caption,headers,rows)=>`<div class="tabelle"><table><caption>${caption}</caption><thead><tr>${headers.map(x=>`<th>${x}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr>${r.map(x=>`<td>${x}</td>`).join('')}</tr>`).join('\n')}</tbody></table></div>\n`;
 const task=(n,exam,no,pts,question,answer)=>{const season=exam[0]==='H'?'Herbst':'Frühjahr',year='20'+exam.slice(1),src=`ihk-ap1-${exam[0].toLowerCase()}${year}`;return `<article class="aufgabe" id="${id}-original-${n}"><p class="herkunft">AP1 ${season} ${year}, Aufgabe ${no}, ${pts} Punkte, sinngemäß wiedergegeben${q(src)}</p><div class="text">${question}</div><details><summary>Lösung mit Punktelogik</summary><div class="inhalt">${answer}</div></details></article>\n`;};
 const variant=(n,label,question,answer)=>`<article class="aufgabe" id="${id}-variante-${n}"><p class="herkunft">Variante zu ${label}</p><div class="text">${question}</div><details><summary>Lösung</summary><div class="inhalt">${answer}</div></details></article>\n`;
 const checks=items=>`<ol class="selbstcheck">${items.map(([a,b])=>`<li>${a}<details><summary>Antwort</summary><div class="inhalt"><p>${b}</p></div></details></li>`).join('\n')}</ol>`;
 const save=parts=>{const matrix=fs.readFileSync(path.join(root,'notizen/MATRIX.md'),'utf8').split(`### ${id.toUpperCase()} ·`)[1].split('\n### ')[0];const entries=[...matrix.matchAll(/([HF])(\d{2}) (\d+\.\d+) \((\d+) P\)/g)];const exams=new Map();for(const m of entries){const key=m[1]+m[2];if(!exams.has(key))exams.set(key,{tasks:[],sum:0});exams.get(key).tasks.push(m[3]);exams.get(key).sum+=+m[4];}const kam=[...exams].map(([e,v])=>`<span>AP1 ${e[0]==='H'?'Herbst':'Frühjahr'} 20${e.slice(1)}, ${v.tasks.join(', ')} (${v.sum} P)</span>`).join(' · ');
 let s=`<section class="kapitel" id="${id}" data-gruppe="B"><header class="kapitel-kopf"><p class="kapitel-nr">${id.toUpperCase()} · Erklären</p><h2>${title}</h2><p class="kam-dran">Kam dran: ${kam}</p><label class="sitzt"><input type="checkbox" data-key="${id}"> Sitzt</label></header>\n`;
 for(const[key,title]of [['worum','Worum es geht'],['begriffe','Begriffe'],['kern','Die Sache'],['original','So hat die IHK gefragt'],['variante','Jetzt du'],['selbstcheck','Selbstcheck']])s+=`<section id="${id}-${key}"><h3>${title}</h3>${parts[key]}</section>\n`;
 s+=`<section id="${id}-quellen"><h3>Quellen dieses Kapitels</h3><ol class="quellenliste">`;
 for(const[key,n]of used){const c=sources.get(key);s+=`<li id="${id}-q${n}" data-src="${key}"><span class="typ">${esc(c[2])}</span> ${esc(c[3])}. Fundstelle: ${esc(c[7])}. ${c[4].startsWith('https://')&&c[5]==='geprüft'?`<a href="${esc(c[4])}">${esc(new URL(c[4]).hostname)}</a> <span class="abruf">(abgerufen ${c[6]})</span>`:'<span class="abruf">(nicht online geprüft)</span>'}</li>`;}s+='</ol></section></section>\n';const filename=`${19+Number(id.slice(1))}-${id}.html`;fs.writeFileSync(path.join(root,'kapitel',filename),s);console.log('Gespeichert: '+filename);};
 return {q,p,card,fig,table,task,variant,checks,save};
}
const txt=(x,y,s,cls='')=>`<text x="${x}" y="${y}" class="${cls||'mitte'}">${esc(s)}</text>`;
const box=(x,y,w,h,label,cls='w')=>`<rect class="${cls}" x="${x}" y="${y}" width="${w}" height="${h}"/>`+txt(x+w/2,y+h/2+5,label);
const arrow=(x1,y1,x2,y2)=>`<line class="l" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" marker-end="url(#pfeil)"/>`;
module.exports={chapter,txt,box,arrow,root};
