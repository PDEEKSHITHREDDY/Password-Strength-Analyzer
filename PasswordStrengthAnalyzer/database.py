import sqlite3
import hashlib


class PasswordDatabase:

    def __init__(self, db_name="password_history.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def password_exists(self, password):
        password_hash = self.hash_password(password)

        self.cursor.execute(
            "SELECT * FROM password_history WHERE password_hash=?",
            (password_hash,)
        )

        return self.cursor.fetchone() is not None

    def save_password(self, password):
        password_hash = self.hash_password(password)

        self.cursor.execute(
            "INSERT INTO password_history(password_hash) VALUES(?)",
            (password_hash,)
        )

        self.connection.commit()