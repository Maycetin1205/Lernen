from pathlib import Path
import html
import re


ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "notizen" / "Y1-UEBERSCHRIFTEN.md"


def main() -> None:
    rows = []
    for line in TABLE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or "| Datei |" in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4 or not cells[3]:
            continue
        rows.append(tuple(cells))

    changed_files = set()
    for filename, section_id, old, new in rows:
        path = ROOT / "kapitel" / filename
        source = path.read_text(encoding="utf-8")
        pattern = re.compile(
            rf'(<h4\s+id="{re.escape(section_id)}">){re.escape(html.escape(old, quote=False))}(</h4>)'
        )
        if len(pattern.findall(source)) != 1:
            raise RuntimeError(f"{filename}: Anker {section_id!r} mit Alttext nicht genau einmal gefunden")
        updated = pattern.sub(rf"\g<1>{html.escape(new, quote=False)}\g<2>", source)
        path.write_text(updated, encoding="utf-8")
        changed_files.add(filename)

    print(f"{len(rows)} Ueberschriften in {len(changed_files)} Kapiteln ersetzt.")
    for filename in sorted(changed_files):
        print(filename)


if __name__ == "__main__":
    main()
