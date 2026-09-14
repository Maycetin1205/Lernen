'use strict';
const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict');
const {execFileSync}=require('node:child_process');
const root=path.resolve(__dirname,'..');
const names=['14-a5','15-a6','16-a7','17-a8','18-a9'];
const read=f=>fs.readFileSync(path.join(root,f),'utf8');
const write=(f,s)=>fs.writeFileSync(path.join(root,f),s);
const appendix=`
## Ergänzende Quellenprüfung K-2, 2026-09-03

| Schlüssel | Kapitel | Typ | Zitat | URL | Status | Abrufdatum | Fundstellen |
|---|---|---|---|---|---|---|---|
| dguv-202-112-elektro | a5 | Behörde | DGUV: Information 202-112, Sicheres und gesundes Arbeiten mit digitalen Medien in der Schule, 2020 | https://publikationen.dguv.de/widgets/pdf/download/article/3990 | geprüft | 2026-09-03 | Abschnitt 2.2, S. 7–9: Belastbarkeit, Kaskadenbildung, Leitungsschutz |
| python-glossary-bytecode | a7 | Hersteller | Python Software Foundation: Python-Glossar | https://docs.python.org/3/glossary.html | geprüft | 2026-09-03 | bytecode, interpreted: Übersetzung in Bytecode und Interpretation |
| oracle-jls-expressions | a7 | Hersteller | Oracle: Java Language Specification, Java SE 21, Chapter 15 | https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html | geprüft | 2026-09-03 | §15.10.4 Arrayzugriff, §15.17.2 Ganzzahldivision |
| postgres-constraints | a9 | Hersteller | PostgreSQL Global Development Group: PostgreSQL 18 Documentation, Constraints | https://www.postgresql.org/docs/current/ddl-constraints.html | geprüft | 2026-09-03 | §5.5, insbesondere 5.5.5: zusammengesetzte und selbstreferenzielle Fremdschlüssel, Eindeutigkeit |
| ms-normalisierung | a9 | Hersteller | Microsoft: Database normalization description | https://learn.microsoft.com/en-us/previous-versions/troubleshoot/microsoft-365/microsoft-365-apps/access/database-normalization-description | geprüft | 2026-09-03 | Erste bis dritte Normalform |
`;
if(!read('notizen/QUELLEN-A.md').includes('| python-glossary-bytecode |'))fs.appendFileSync(path.join(root,'notizen/QUELLEN-A.md'),appendix);
// Kürzen redundanter Formulierungen, ohne Verfahren oder Aufgaben zu entfernen.
const cuts={
 '15-a6':[['Die Formel steht meist im Heft, weil die Aufgabenstelle die Verwechslung kennt. Sie zu lesen kostet nichts.','Nutze die Formel im Aufgabenheft.']],
 '16-a7':[['Nicht überspringen, nicht raten. Er wirkt umständlich, findet aber genau die Fehler, die ein Blick auf den Quelltext übersieht.','Protokolliere jeden Durchlauf, statt das Endergebnis zu schätzen.'],['Eine Suche darin braucht zwei ineinanderliegende Schleifen. Häufigster Denkfehler:','Im gezeigten Verfahren suchen zwei verschachtelte Schleifen. Die Falle:'],['Der bloße Name einer Sprache ist kein Kriterium.','Ein Sprachname allein genügt nicht.'],['Die Austrittszeile gehört dazu: i steht auf 5, die Bedingung ist falsch, die Schleife endet.','Beim Austritt steht i auf 5; die Bedingung ist falsch.']],
 '18-a9':[['Der Service eines IT-Systemhauses führt seine Störungsmeldungen in einer einzigen Tabelle. Bei jedem neuen Ticket tippt der Techniker Firma, Straße und Telefonnummer des Kunden erneut ein. Als eine Kanzlei umzieht, steht die alte Anschrift noch in vierzehn Zeilen; der Monteur fährt zur falschen Adresse. Genau das verhindert ein sauberes Datenmodell.','Ein Systemhaus speichert Kundenanschriften in jeder Ticketzeile erneut. Nach einem Umzug bleibt die alte Adresse in vierzehn Zeilen stehen; der Monteur fährt falsch. Ein sauberes Datenmodell vermeidet solche widersprüchlichen Kopien.'],['Redundanzfrei heißt hier: Der Vorname beschreibt den Mitarbeiter, nicht den Auftrag. Stünde er am Auftrag, wäre er bei jedem weiteren Auftrag desselben Mitarbeiters erneut gespeichert. Beginn und Ende beschreiben umgekehrt den Auftrag. Die Beziehung ist 1:n, weil ein Mitarbeiter mehrere Aufträge bearbeitet, ein Auftrag aber nur von einem.','Der Vorname gehört zum Mitarbeiter und wird dort einmal gespeichert. Beginn und Ende gehören zum Auftrag. Ein Mitarbeiter bearbeitet mehrere Aufträge, jeder Auftrag gehört genau einem Mitarbeiter: 1:n.'],['Die Telefonnummer gehört zum Techniker. Stünde sie am Einsatz, wäre sie bei jedem weiteren Einsatz erneut gespeichert, und eine neue Nummer müsste an vielen Stellen nachgezogen werden. Beginn und Ende gehören zum Einsatz. Zusammen 6 Punkte.','Die Telefonnummer gehört zum Techniker; Beginn und Ende gehören zum Einsatz. So wird eine Telefonnummer nur einmal geändert. Zusammen 6 Übungspunkte.'],['Alle vier Angaben liegen in derselben Tabelle, ein JOIN entfällt. Die Reihenfolge der mit AND verbundenen Bedingungen ist beliebig, der Betrag wird ohne Tausenderpunkt und ohne Währungszeichen geschrieben.','Alle Angaben liegen in einer Tabelle. AND-Bedingungen dürfen ihre Reihenfolge wechseln; SQL-Zahlen tragen keinen Tausenderpunkt und kein Währungszeichen.']]
};
for(const [n,pairs]of Object.entries(cuts)){let s=read('kapitel/'+n+'.html');for(const[a,b]of pairs)s=s.replace(a,b);write('kapitel/'+n+'.html',s);}
const log=[];
const round=x=>Math.round(x*100)/100;
for(const [name,input,value,expected] of [
 ['A5 H21 Leistung','60/0.76',round(60/.76),78.95],['A5 H21 Kosten A','180*0.13953*0.30',round(180*.13953*.30),7.53],['A5 H21 Kosten B','180*0.07894*0.30',round(180*.07894*.30),4.26],['A5 H21 Amortisation','ceil(100/3.27)',Math.ceil(100/3.27),31],['A5 F24 Netzteil','ceil(560*1.10/50)*50',Math.ceil(560*1.1/50)*50,650],['A5 Variante Netzteil','ceil(489*1.15/50)*50',Math.ceil(489*1.15/50)*50,600],['A5 Variante Amortisation','ceil(80/3.71)',Math.ceil(80/3.71),22],['A5 Schema','round((round(0.07471*1760)+0.003*3520)*0.32)',round((round(.07471*1760)+.003*3520)*.32),45.46],['A8 Variante Notebook','12*5',12*5,60],['A8 Variante Beamer mit Pauschale','25*5+10',25*5+10,135],['A9 Paare','40*12',40*12,480]
]){assert.equal(value,expected,name);log.push(`${name}: ${input} = ${value}`);}
function cpm(d,p){const a=d.map((dur,i)=>({id:String.fromCharCode(65+i),dur,pred:p[i],succ:[],faz:0}));a.forEach((v,i)=>v.pred.forEach(j=>a[j].succ.push(i)));a.forEach(v=>{v.faz=Math.max(0,...v.pred.map(j=>a[j].fez));v.fez=v.faz+v.dur;});const T=Math.max(...a.map(v=>v.fez));a.toReversed().forEach(v=>{v.sez=v.succ.length?Math.min(...v.succ.map(j=>a[j].saz)):T;v.saz=v.sez-v.dur;v.gp=v.saz-v.faz;v.fp=(v.succ.length?Math.min(...v.succ.map(j=>a[j].faz)):T)-v.fez;assert.equal(v.gp,v.sez-v.fez);});return {T,a};}
const preds11=[[],[0],[1],[1],[1],[1],[2,3],[4],[6,7],[8],[5,9]],preds10=[[],[0],[1],[1],[2,3],[4],[1],[6],[4],[5,8,7]];
const plans=[['Beispiel',[3,6,2,2,6,2],[[],[0],[0],[2],[1,3],[4]],17],['H21',[2,4,3,8,2,5,4,1,3,1,2],preds11,24],['Variante H21',[3,5,4,9,3,6,5,2,4,2,3],preds11,31],['F25',[2,25,32,40,70,15,8,2,16,4],preds10,157],['Variante F25',[3,20,25,35,60,12,6,3,18,5],preds10,141]];
for(const[n,d,p,t]of plans){const r=cpm(d,p);assert.equal(r.T,t);log.push(`A6 ${n}: Dauer ${r.T}; kritisch ${r.a.filter(v=>v.gp===0).map(v=>v.id).join('-')}`);log.push(JSON.stringify(r.a));}
let summe=0,gross=0;for(const x of [12,7,25,9,18]){summe+=x;if(x>10)gross++;}assert.equal(summe,71);assert.equal(gross,3);log.push('A7 Akkumulator: [12,7,25,9,18] -> Summe 71, Zähler 3');
const field=[[1,223,312,154,47,124,236,334],[2,103,401,14,236,56],[3,20,312,235,17,124,32]];assert.equal(field.some(r=>r[0]===3&&r.slice(1).includes(236)),false);log.push('A7 H24: Person 3 / Raum 236 -> false');
write('notizen/k2-pruefung/NACHRECHNUNG.txt',log.join('\n')+'\n');
const summary=[];const allIds=new Set();let joined='';
for(const n of names){const s=read('kapitel/'+n+'.html');const result=execFileSync(process.execPath,[path.join(__dirname,'check.js'),path.join(root,'kapitel',n+'.html'),'--fragment'],{encoding:'utf8'});summary.push(n+': '+result.trim());for(const m of s.matchAll(/\bid="([^"]+)"/g)){assert(!allIds.has(m[1]),m[1]);allIds.add(m[1]);}joined+=s+'\n';}
const sources=read('notizen/QUELLEN-A.md')+read('notizen/QUELLEN-B.md');for(const m of joined.matchAll(/href="(https?:[^\"]+)"/g))assert(sources.split('\n').some(l=>l.includes(m[1])&&l.includes('| geprüft |')&&l.includes('2026-09-03')),m[1]);
const head=read('kapitel/00-kopf.html');write('K2-vorschau.html',head+'\n<section class="teil" id="k2-stand"><h2>Arbeitsstand K-2</h2><p>Kapitel A5 bis A9. Die Gesamtdatei wird nach den weiteren Bauphasen zusammengesetzt.</p></section>\n'+joined+read('kapitel/99-fuss.html'));
// Kompakte Grafikansicht für die Sichtprüfung, mit unverändertem CSS.
const css=head.match(/<style>[\s\S]*?<\/style>/)[0],defs=head.match(/<svg[\s\S]*?<\/svg>/)[0];
write('notizen/k2-pruefung/grafiken.html','<!doctype html><html lang="de"><meta charset="utf-8">'+css+'<body><main>'+defs+joined.match(/<figure class="abb">[\s\S]*?<\/figure>/g).join('\n')+'</main></body></html>');
write('notizen/k2-pruefung/VALIDIERUNG.txt',summary.join('\n')+'\nKapitelübergreifende IDs eindeutig; Quellen-URLs in geprüfter Quellenliste vorhanden.\n');
console.log(summary.join('\n'));console.log('Nachrechnungen, Quellenprüfung und lokale Vorschau gespeichert.');
