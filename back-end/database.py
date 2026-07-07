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

conn.commit()
conn.close()

print("Database created!")