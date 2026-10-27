import sys
from pathlib import Path

from tabulate import tabulate

NAME, SURNAME, GROUP = "Vlad", "Kudryk", "IT-32"

print(f"{NAME} {SURNAME}, {GROUP}")

path = Path(__file__).parent / "data" / "expenses.csv"
if not path.is_file():
    print(f"error: {path} not found", file=sys.stderr)
    sys.exit(1)

stats = {}  # категорія -> [кількість, сума]
for n, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split(";")
    try:
        category = parts[1].strip()
        amount = float(parts[2].strip().replace(",", "."))
    except (ValueError, IndexError):
        print(f"warning: line {n} skipped: {line}", file=sys.stderr)
        continue
    item = stats.setdefault(category, [0, 0.0])
    item[0] += 1
    item[1] += amount

rows = [[cat, cnt, total] for cat, (cnt, total) in stats.items()]
rows.append(["TOTAL", sum(r[1] for r in rows), sum(r[2] for r in rows)])

print(tabulate(rows, headers=["category", "count", "total"],
               tablefmt="github", floatfmt=".2f"))