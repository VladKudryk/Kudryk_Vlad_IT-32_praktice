import math
import random
from datetime import datetime
from pathlib import Path

NAME, SURNAME, GROUP = "Vlad", "Kudryk", "IT-32"
YEAR = 2009
print(f"{NAME} {SURNAME}, {GROUP}")

random.seed(YEAR)

r = random.randint(5, 20)
n1 = random.randint(4, 7)
g = random.randint(2, 9)
a, b = g * random.randint(2, 9), g * random.randint(2, 9)
n2, k = random.randint(5, 9), random.randint(2, 4)
p = random.choice([5, 10, 15, 20, 25])
base = 20 * random.randint(5, 25)

questions = [
    (f"sqrt({r * r})", math.isqrt(r * r)),
    (f"{n1}!", math.factorial(n1)),
    (f"gcd({a}, {b})", math.gcd(a, b)),
    (f"comb({n2}, {k})", math.comb(n2, k)),
    (f"{p}% of {base}", p * base // 100),
]

start = datetime.now()
score = 0
for i, (text, answer) in enumerate(questions, 1):
    try:
        reply = input(f"{i}) {text} = ")
    except EOFError:
        reply = ""
    try:
        ok = int(reply.strip()) == answer
    except ValueError:
        ok = False
    if ok:
        score += 1
        print("   correct")
    else:
        print(f"   wrong, answer: {answer}")
end = datetime.now()
seconds = (end - start).total_seconds()
print(f"score: {score}/{len(questions)}, time: {seconds:.1f} s")

results = Path(__file__).parent / "results"
results.mkdir(exist_ok=True)
history = results / "history.csv"
new_file = not history.exists()
with history.open("a", encoding="utf-8") as f:
    if new_file:
        f.write("# datetime;score;seconds\n")
    f.write(f"{start:%Y-%m-%d %H:%M};{score};{seconds:.1f}\n")

attempts = []
for line in history.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    dt, sc, sec = line.split(";")
    attempts.append((int(sc), float(sec), dt))
best = min(attempts, key=lambda x: (-x[0], x[1]))
print(f"attempts: {len(attempts)}, best: {best[0]}/{len(questions)} in {best[1]:.1f} s ({best[2]})")