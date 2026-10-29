
def parse_line(line):
    parts = line.strip().split(";")

    if len(parts) != 4:
        raise ValueError("Неправильна кількість полів")

    return {
        "date": parts[0],
        "category": parts[1],
        "amount": float(parts[2]),
        "comment": parts[3],
    }


def total_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]

    return {category: round(total, 2) for category, total in totals.items()}


def load_expenses(path):
    records = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line and not line.startswith("#"):
                records.append(parse_line(line))

    return records
