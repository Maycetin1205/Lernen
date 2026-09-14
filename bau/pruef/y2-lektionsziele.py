from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notizen"

LESSONS = {
    "a1-original-1": "a1-k7", "a1-original-2": "a1-k7",
    "a2-original-1": "a2-k7", "a2-original-2": "a2-k4",
    "a3-original-1": "a3-k4", "a3-original-2": "a3-k3",
    "a4-original-1": "a4-k4", "a4-original-2": "a4-k5",
    "a5-original-1": "a5-k6", "a5-original-2": "a5-k5", "a5-original-3": "a5-k7",
    "a6-original-1": "a6-k9", "a6-original-2": "a6-k9",
    "a7-original-1": "a7-k3", "a7-original-2": "a7-k9", "a7-original-3": "a7-k11",
    "a8-original-1": "a8-k4", "a8-original-2": "a8-k5", "a8-original-3": "a8-k3", "a8-original-4": "a8-k3",
    "a9-original-1": "a9-k9", "a9-original-2": "a9-k9", "a9-original-3": "a9-k12",
    "b1-original-1": "b1-k3", "b1-original-2": "b1-k6", "b1-original-3": "b1-k9",
    "b2-original-1": "b2-k3", "b2-original-2": "b2-k2", "b2-original-3": "b2-k4",
    "b3-original-1": "b3-k4", "b3-original-2": "b3-k2",
    "b4-original-1": "b4-k2", "b4-original-2": "b4-k4", "b4-original-3": "b4-k6",
    "b5-original-1": "b5-k6", "b5-original-2": "b5-k13", "b5-original-3": "b5-k2",
    "b6-original-1": "b6-k8", "b6-original-2": "b6-k10", "b6-original-3": "b6-k2",
    "b7-original-1": "b7-k5", "b7-original-2": "b7-k8", "b7-original-3": "b7-k4",
    "b8-original-1": "b8-k9", "b8-original-2": "b8-k3", "b8-original-3": "b8-k3",
    "b9-original-1": "b9-k3", "b9-original-2": "b9-k6", "b9-original-3": "b9-k4",
    "b10-original-1": "b10-k7", "b10-original-2": "b10-k6", "b10-original-3": "b10-k2",
    "b11-original-1": "b11-k2", "b11-original-2": "b11-k8", "b11-original-3": "b11-k1",
}


def main() -> None:
    used = set()
    changed_files = 0
    changed_entries = 0
    for path in sorted(NOTES.glob("WEGWEISER-[ab][0-9]*.json")):
        entries = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for entry in entries:
            target = entry.get("ziel", "")
            if "-original-" not in target:
                continue
            if target not in LESSONS:
                raise RuntimeError(f"Kein Lektionsziel für {path.name}: {target}")
            entry["lektion"] = LESSONS[target]
            used.add(target)
            changed = True
            changed_entries += 1
        if changed:
            path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed_files += 1
    unused = set(LESSONS) - used
    if unused:
        raise RuntimeError(f"Nicht verwendete Zuordnungen: {sorted(unused)}")
    print(f"{changed_entries} Original-Zeilen in {changed_files} Wegweiser-Dateien mit Lektionsziel ergänzt.")


if __name__ == "__main__":
    main()
