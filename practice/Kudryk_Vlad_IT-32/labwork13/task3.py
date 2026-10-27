import math
import sys
from datetime import datetime
from pathlib import Path

NAME, SURNAME, GROUP = "Vlad", "Kudryk", "IT-32"

print(f"{NAME} {SURNAME}, {GROUP}")

USAGE = "usage: python3 task3.py [--dry-run] <dir>"
args = sys.argv[1:]
dry = "--dry-run" in args
rest = [a for a in args if a != "--dry-run"]
if len(rest) != 1 or rest[0].startswith("--"):
    print(USAGE)
    sys.exit(2)

root = Path(rest[0])
if not root.is_dir():
    print(f"error: {root} is not a directory", file=sys.stderr)
    sys.exit(1)


def human(size: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    idx = 0 if size < 1 else min(int(math.log(size, 1024)), len(units) - 1)
    return f"{size / 1024 ** idx:.1f} {units[idx]}"


files = []
for p in root.iterdir():
    if p.is_file():
        st = p.stat()
        files.append((p, st.st_size, datetime.fromtimestamp(st.st_mtime)))
files.sort(key=lambda x: x[2])

if not files:
    print("no files to organize")
    sys.exit(0)

plan = []
for p, size, mtime in files:
    target = root / mtime.strftime("%Y-%m") / p.name
    if target.exists():
        print(f"error: {target} already exists, nothing was moved", file=sys.stderr)
        sys.exit(1)
    plan.append((p, size, mtime, target))

width = max(len(p.name) for p, *_ in plan)
lines = []
for p, size, mtime, target in plan:
    lines.append(f"{p.name:<{width}} {human(size):>9}  {mtime:%d.%m.%Y %H:%M}  -> {target.parent.name}/")
folders = len({t.parent.name for *_, t in plan})
for line in lines:
    print(line)

if dry:
    print(f"{len(plan)} files, {folders} folders (dry run, nothing moved)")
    sys.exit(0)

for p, size, mtime, target in plan:
    target.parent.mkdir(exist_ok=True)
    p.rename(target)
print(f"{len(plan)} files, {folders} folders")

reports = Path(__file__).parent / "reports"
reports.mkdir(exist_ok=True)
report = reports / f"organize_{datetime.now():%Y%m%d_%H%M}.txt"
report.write_text("\n".join(lines) + f"\n{len(plan)} files, {folders} folders\n", encoding="utf-8")
print(f"report saved to: reports/{report.name}")