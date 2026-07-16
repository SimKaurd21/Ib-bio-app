import sqlite3

conn = sqlite3.connect("ib_biology.db")
cursor = conn.cursor()

print("Users:")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

print("\nReview Cards:")
cursor.execute("SELECT * FROM review_cards")
rows = cursor.fetchall()

print("\nAnswers:")
cursor.execute("SELECT * FROM user_answers")
meow = cursor.fetchall()

for row in rows:
    print(row)

for meows in meow:
    print(meows)

conn.close()