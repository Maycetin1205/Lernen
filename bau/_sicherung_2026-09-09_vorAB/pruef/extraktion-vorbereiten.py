from pathlib import Path
import shutil, subprocess, fitz, json
base=Path(r'C:\Users\mu.aycetin\Desktop\Projekte\Porjekte\AP1')
ocr=base/'PrüfungenOCR'
sol=base/'Lerndateien'/'Informationen'/'FISI AP1 & AP2'/'Prüfungen'/'Prüfungen AP1'/'AP1 und Zwischenprüfungen'/'AP1 (Neue Prüfungsordnung)'
bau=Path(r'C:\Users\mu.aycetin\Desktop\Lernen\bau')
jobs=[('e3','2025 Herbst*','Ap1 2025/*Herbst_2025/Ap1_Lösung (1).pdf')]
for ident,og,sg in jobs:
    d=bau/'notizen'/('scratch-'+ident);d.mkdir(exist_ok=True)
    task=next(ocr.glob(og)); solution=next(sol.glob(sg))
    report=[]
    for name,src in [('aufgaben',task),('loesung',solution)]:
        dst=d/(name+'.pdf'); shutil.copyfile(src,dst)
        subprocess.run([r'C:\Program Files\Git\mingw64\bin\pdftotext.exe','-layout','-enc','UTF-8',str(dst),str(d/(name+'.txt'))],check=True)
        doc=fitz.open(src)
        for i,page in enumerate(doc):
            page.get_pixmap(dpi=150).save(str(d/f'{name}-{i+1:02}.png'))
        report.append({'source':str(src),'pages':len(doc),'prefix':str(d/name)})
    (d/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(ident, len(report), "PDFs prepared",flush=True)

