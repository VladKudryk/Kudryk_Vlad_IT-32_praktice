import math
import sys
from datetime import date, timedelta
from pathlib import Path

NAME, SURNAME, GROUP = "Vlad", "Kudryk", "IT-32"

print(f"{NAME} {SURNAME}, {GROUP}")


def days_in_month(d: date) -> int:
    first = d.replace(day=1)
    if d.month == 12:
        nxt = date(d.year + 1, 1, 1)
    else:
        nxt = date(d.year, d.month + 1, 1)
    return (nxt - first).days


assert days_in_month(date(2026, 12, 15)) == 31
assert days_in_month(date(2028, 2, 10)) == 29

path = Path(__file__).parent / "data" / "expenses.csv"
if not path.is_file():
    print(f"error: {path} not found", file=sys.stderr)
    sys.exit(1)

by_date = {}
for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split(";")
    try:
        d = date.fromisoformat(parts[0].strip())
        amount = float(parts[2])
    except (ValueError, IndexError):
        print(f"warning: line {n} skipped: {line}", file=sys.stderr)
        continue
    by_date[d] = by_date.get(d, 0.0) + amount

if not by_date:
    print("error: no valid expenses", file=sys.stderr)
    sys.exit(1)

first, last = min(by_date), max(by_date)
period = (last - first).days + 1
print(f"period: {first:%d.%m.%Y} ({first:%A}) - {last:%d.%m.%Y} ({last:%A}), {period} days")

names = [(date(2024, 1, 1) + timedelta(days=i)).strftime("%A") for i in range(7)]
week = [0.0] * 7
for d, v in by_date.items():
    week[d.weekday()] += v
print()
print(f"{'weekday':<12} {'total':>8}")
for name, v in zip(names, week):
    print(f"{name:<12} {v:>8.2f}")

daily = [by_date.get(first + timedelta(days=i), 0.0) for i in range(period)]
total = math.fsum(daily)
mean = total / period
std = math.sqrt(math.fsum((x - mean) ** 2 for x in daily) / period)
top = max(by_date, key=by_date.get)
no_spend = sum(1 for x in daily if x == 0)

print()
print(f"total:        {total:.2f}")
print(f"per day:      {mean:.2f} +- {std:.2f}")
print(f"top day:      {top:%d.%m.%Y} ({top:%A}), {by_date[top]:.2f}")
print(f"no-spend days: {no_spend}")

dim = days_in_month(last)
print(f"days in {last:%B}: {dim}, left after {last:%d.%m}: {dim - last.day}")
print(f"month forecast: {mean * dim:.2f}")