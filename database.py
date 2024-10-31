# database.py
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                amount REAL
            )
        """)
        self.conn.commit()

    def insert_expense(self, date, category, amount):
        self.cursor.execute("INSERT INTO expenses VALUES (NULL, ?, ?, ?)", (date, category, amount))
        self.conn.commit()

    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
