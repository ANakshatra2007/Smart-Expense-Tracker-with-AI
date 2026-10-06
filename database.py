import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_NAME = DATA_DIR / "expenses.db"


def create_table():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(str(DATABASE_NAME))
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            payment_method TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(expense_date, amount, category, description, payment_method):
    connection = sqlite3.connect(str(DATABASE_NAME))
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (expense_date, amount, category, description, payment_method)
        VALUES (?, ?, ?, ?, ?)
    """, (
        expense_date,
        amount,
        category,
        description,
        payment_method
    ))

    connection.commit()
    connection.close()


def get_expenses():
    connection = sqlite3.connect(str(DATABASE_NAME))
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM expenses
        ORDER BY expense_date DESC
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses

