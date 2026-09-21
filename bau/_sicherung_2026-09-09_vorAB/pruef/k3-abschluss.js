'use strict';
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto'),cp=require('node:child_process');
const root=path.resolve(__dirname,'..');
function edit(file,oldText,newText){const f=path.join(root,file),s=fs.readFileSync(f,'utf8');if(s.includes(newText))return;if(s.includes(oldText))fs.writeFileSync(f,s.replace(oldText,newText));else throw Error('Text nicht gefunden: '+file);}
edit('pruef/k3-b4.js','und Vorlageneinzug','und Dokumenteneinzug');
edit('pruef/k3-b2.js','Beide besitzen ein öffentliches und ein privates Schlüsselpaar.','Beide besitzen jeweils ein Schlüsselpaar aus öffentlichem und privatem Schlüssel.');
edit('pruef/k3-b2.js',"<pre><code>F68F966BA322A4245ACE6A35C58F8F2CD263F89EFED8B16F53ACDD868976252F</code></pre>","<p><code>F68F966BA322A4245ACE6A35C58F8F2CD<wbr>263F89EFED8B16F53ACDD868976252F</code></p>");
edit('pruef/k3-b3.js','arrow(68,77,68,182)+txt(133,126,\'Auskunft verlangen\')+arrow(207,182,207,77)+txt(123,160,\'Auskunft erteilen\')','arrow(40,77,40,182)+txt(140,118,\'Auskunft verlangen\')+arrow(240,182,240,77)+txt(140,153,\'Auskunft erteilen\')');
edit('pruef/k3-b3.js','außer ein Risiko für Rechte und Freiheiten ist voraussichtlich ausgeschlossen.','außer es besteht voraussichtlich kein Risiko für Rechte und Freiheiten.');
edit('notizen/QUELLEN-B.md','Kurzpapier Nr. 1 (Auslegung der DSGVO-Grundsätze); Kurzpapier Nr. 13 (Auftragsverarbeiter)','Kurzpapier Nr. 1 (Verzeichnis von Verarbeitungstätigkeiten); Kurzpapier Nr. 13 (Auftragsverarbeiter)');
// Ergänzende Belege an den Aussagen registrieren, damit sie in der Quellenliste erscheinen.
edit('pruef/k3-b2.js',"'rfc-2865')","'rfc-2865')+p('WPA3-Personal wird auch als WPA3-SAE bezeichnet; die konkrete Unterstützung hängt vom Gerät und seiner Software ab.','intel-wpa3')");
edit('pruef/k3-b2.js',"bereits kompromittierten Endgeräte.','bsi-tr-02102-1');","bereits kompromittierten Endgeräte.'+q('rfc-9580'),'rfc-8551');");
edit('pruef/k3-b2.js',"während SSH insbesondere sichere Fernadministration ermöglicht.'","während SSH insbesondere sichere Fernadministration ermöglicht.'+q('rfc-8446')+q('rfc-4301')");
edit('pruef/k3-b3.js',"Für Maßnahmen auf einen Antrag gilt grundsätzlich die Monatsfrist aus Art. 12 Abs. 3.'","Für Maßnahmen auf einen Antrag gilt grundsätzlich die Monatsfrist aus Art. 12 Abs. 3.'+c.q('bmf-dsgvo-auszug','Art. 12 Abs. 3')");
const chapters=['20-b1.html','21-b2.html','22-b3.html','23-b4.html'];
for(let i=1;i<=4;i++)cp.execFileSync(process.execPath,[path.join(__dirname,`k3-b${i}.js`)],{stdio:'inherit'});
const report=[];
const matrix=fs.readFileSync(path.join(root,'notizen/MATRIX.md'),'utf8');
const allIds=new Set();
const expectedIds=new Set(fs.readdirSync(path.join(root,'kapitel')).filter(f=>f.endsWith('.html')).flatMap(f=>[...fs.readFileSync(path.join(root,'kapitel',f),'utf8').matchAll(/\bid="([^"]+)"/g)].map(m=>m[1])));
for(let i=1;i<=11;i++)expectedIds.add('b'+i);
for(const file of chapters){
 const f=path.join(root,'kapitel',file),s=fs.readFileSync(f,'utf8'),id=file.slice(3,-5);
 const output=cp.execFileSync(process.execPath,[path.join(__dirname,'check.js'),f,'--fragment'],{encoding:'utf8'}).trim();
 if(!output.includes('Keine Fehler.'))throw Error(output);
 const words=s.replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/&[a-z#0-9]+;/g,' ').split(/\s+/).filter(Boolean).length;
 const count=re=>(s.match(re)||[]).length;
 for(const m of s.matchAll(/\bid="([^"]+)"/g)){if(allIds.has(m[1]))throw Error('Doppelte ID '+m[1]);allIds.add(m[1]);}
 for(const m of s.matchAll(/href="#([^"]+)"/g))if(!expectedIds.has(m[1]))throw Error('Linkziel unbekannt '+m[1]);
 const block=matrix.split(`### ${id.toUpperCase()} ·`)[1].split('\n### ')[0],expected=new Map();
 for(const m of block.matchAll(/([HF])(\d{2}) (\d+\.\d+) \((\d+) P\)/g)){const key=m[1]+m[2];if(!expected.has(key))expected.set(key,{nums:[],pts:0});expected.get(key).nums.push(m[3]);expected.get(key).pts+=+m[4];}
 const actual=[...s.matchAll(/<span>AP1 (Herbst|Frühjahr) 20(\d{2}), ([\d., ]+) \((\d+) P\)<\/span>/g)];
 if(actual.length!==expected.size)throw Error('Kam-dran-Anzahl '+id);
 for(const m of actual){const e=expected.get((m[1]==='Herbst'?'H':'F')+m[2]);if(!e||e.nums.join(', ')!==m[3]||e.pts!==+m[4])throw Error('Kam-dran-Abweichung '+id);}
 const result={file,words,cards:count(/<dl class="begriff"/g),figures:count(/<figure class="abb">/g),originals:count(/id="b\d-original-\d"/g),variants:count(/id="b\d-variante-\d"/g),questions:4,sources:count(/data-src="/g),validation:output};
 report.push(result);console.log(JSON.stringify(result));
}
const hashes=JSON.parse(fs.readFileSync(path.join(root,'notizen/FESTE-BAUTEILE-SHA256.json'),'utf8'));
for(const item of hashes){const actual=crypto.createHash('sha256').update(fs.readFileSync(item.Path)).digest('hex').toUpperCase();if(actual!==item.Hash)throw Error('Fester Bauteil verändert: '+item.Path);}
console.log('Kam-dran-Zeilen, Linkziele, IDs und feste Bauteile geprüft.');
const head=fs.readFileSync(path.join(root,'kapitel/00-kopf.html'),'utf8');
const foot=fs.readFileSync(path.join(root,'kapitel/99-fuss.html'),'utf8');
const preview=head+'\n<p class="klein">Arbeitsansicht K-3: B1 bis B4. Die vollständige Navigation wird in Phase Z mit allen Kapiteln zusammengeführt.</p>\n'+chapters.map(f=>fs.readFileSync(path.join(root,'kapitel',f),'utf8')).join('\n')+foot;
fs.writeFileSync(path.join(root,'K3-vorschau.html'),preview);
fs.writeFileSync(path.join(root,'notizen/K3-PRUEFUNG.json'),JSON.stringify({date:'2026-09-03',chapters:report,matrix:'stimmt',fixedParts:'SHA256 unverändert',visual:'Browser-Sichtprüfung in Phase Z offen; lokale Navigation zuvor durch Browser-Sicherheitsrichtlinie blockiert'},null,2)+'\n');
