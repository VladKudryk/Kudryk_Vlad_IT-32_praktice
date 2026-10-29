import pytest
from pathlib import Path
from expenses import parse_line, total_by_category, load_expenses

def test_parse_line():
    record = parse_line("2026-10-20;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_comment():
    record = parse_line("2026-10-20;food;85.50;lunch")
    assert record["comment"] == "lunch"


def test_parse_line_bad_fields():
    with pytest.raises(ValueError):
        parse_line("2026-10-20;food;85.50")


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-10-20;food;abc;lunch")


@pytest.mark.parametrize(
    "line, category, amount",
    [
        ("2026-10-20;food;85.50;lunch", "food", 85.5),
        ("2026-10-21;transport;40.00;bus", "transport", 40.0),
        ("2026-10-22;food;14.50;coffee", "food", 14.5),
        ("2026-10-23;transport;30.00;taxi", "transport", 30.0),
        ("2026-10-24;food;120.00;groceries", "food", 120.0),
    ],
)
def test_parse_line_parametrize(line, category, amount):
    record = parse_line(line)
    assert record["category"] == category
    assert record["amount"] == amount


def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date;category;amount;comment\n"
        "2026-10-20;food;85.50;lunch\n"
        "\n"
        "2026-10-22;food;14.50;coffee\n",
        encoding="utf-8",
    )

    records = load_expenses(path)
    assert total_by_category(records) == {"food": 100.0}


def test_real_expenses():
    path = Path(__file__).parent / "data" / "expenses.csv"
    records = load_expenses(path)

    assert total_by_category(records) == {
        "food": 220.0,
        "transport": 70.0,
    }
