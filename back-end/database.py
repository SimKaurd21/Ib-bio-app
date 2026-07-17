from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS review_cards (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    card_id TEXT NOT NULL,
    UNIQUE(user_id, card_id),
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_answers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    card_id TEXT NOT NULL,
    answer_text TEXT,
    UNIQUE(user_id, card_id),
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
cursor.close()
conn.close()

print("PostgreSQL database created!")