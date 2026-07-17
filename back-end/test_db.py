from db import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

print("Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

print("\nReview Cards:")
cursor.execute("SELECT * FROM review_cards")
for row in cursor.fetchall():
    print(row)

print("\nAnswers:")
cursor.execute("SELECT * FROM user_answers")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()