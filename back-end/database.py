import sqlite3

conn = sqlite3.connect('ib_biology.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS review_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    card_id INTEGER NOT NULL,
    UNIQUE(user_id, card_id),
    FOREIGN KEY(user_id) REFERENCES users(id)
    )
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    card_id TEXT NOT NULL,
    answer_text TEXT,
    UNIQUE(user_id, card_id),
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()

print("Database created!")