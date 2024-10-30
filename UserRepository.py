import sqlite3

DB_NAME = "not_telegram.db"


class UserRepository:

    def __init__(self, database=DB_NAME):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.__create_table()

    def __create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL,
                                email TEXT NOT NULL,
                                age INTEGER,
                                balance INTEGER NOT NULL)
                             """)
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return self.cursor.fetchone()

    def add_user(self, username, email, age, balance):
        self.cursor.execute("""INSERT INTO users (username, email, age, balance)
                                VALUES (?, ?, ?, ?)""", (username, email, age, balance))
        self.connection.commit()

    def update__user(self, user_id, username, email, age, balance):
        self.cursor.execute("UPDATE users SET username = ?, email = ?, age = ?, balance = ? WHERE id = ?",
                            (username, email, age, balance, user_id))
        self.connection.commit()

    def update_balance(self, user_id, balance):
        self.cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (balance, user_id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()

    def find_users_by_age_not_equal_to(self, age):
        self.cursor.execute("SELECT * FROM users WHERE age != ?", (age,))
        return self.cursor.fetchall()

    def count(self):
        self.cursor.execute("SELECT COUNT(*) FROM users")
        return self.cursor.fetchone()[0]

    def get_total_balance(self):
        self.cursor.execute("SELECT SUM(balance) FROM users")
        return self.cursor.fetchone()[0]

    def close(self):
        self.connection.close()
