from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import psycopg
from db import get_db_connection
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "IB Biology API running"}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:
        return {"message": "Email and password are required."}, 400

    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute(
            """
            INSERT INTO users (email, password_hash)
            VALUES (%s, %s)
            RETURNING id
            """,
            (email, hashed_password)
        )

        user_id = cursor.fetchone()[0]
        conn.commit()

    except psycopg.errors.UniqueViolation:
        conn.rollback()
        cursor.close()
        conn.close()
        return {"message": "Email already registered"}, 400

    cursor.close()
    conn.close()
    return {
        "message": "User registered",
        "user_id": user_id
    }

@app.route("/login", methods=["POST"])
def login():
    
    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:
        return {"message": "Email and password are required."}, 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, password_hash
        FROM users
        WHERE email = %s
        """,
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return {"message": "Invalid credentials"}, 401

    user_id = user[0]
    stored_hash = user[1]

    if check_password_hash(stored_hash, password):
        return {
            "message": "Login successful",
            "user_id": user_id
        }

    return {"message": "Invalid credentials"}, 401

@app.route("/review", methods=["POST"])
def save_review():
    data = request.get_json()

    user_id = data["user_id"]
    card_id = data["card_id"]

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO review_cards (user_id, card_id)
            VALUES (%s, %s)
            """,
            (user_id, card_id)
        )

        conn.commit()

    except psycopg.errors.UniqueViolation:
        conn.rollback()
        cursor.close()
        conn.close()
        return {"message": "Card already marked"}, 400

    cursor.close()
    conn.close()

    return {"message": "Review card saved"}


@app.route("/review/<int:user_id>", methods=["GET"])
def get_review_cards(user_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT card_id
        FROM review_cards
        WHERE user_id = %s
        """,
        (user_id,)
    )

    cards = cursor.fetchall()

    cursor.close()
    conn.close()

    review_cards = [card[0] for card in cards]

    return {
        "review_cards": review_cards
    }

@app.route("/review/<int:user_id>/<card_id>", methods=["DELETE"])
def delete_review_card(user_id, card_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM review_cards
        WHERE user_id = %s
        AND card_id = %s
        """,
        (user_id, card_id)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Review card removed"
    }

@app.route("/user_answers", methods=["POST"])
def save_user_answer():
    data = request.get_json()

    user_id = data["user_id"]
    card_id = data["card_id"]
    answer = data["answer"]

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO user_answers (user_id, card_id, answer_text)
            VALUES (%s, %s, %s)
            """,
            (user_id, card_id, answer)
        )

        conn.commit()

    except psycopg.errors.UniqueViolation:
        conn.rollback()

        cursor.execute(
            """
            UPDATE user_answers
            SET answer_text = %s
            WHERE user_id = %s
            AND card_id = %s
            """,
            (answer, user_id, card_id)
        )

        conn.commit()

    cursor.close()
    conn.close()

    return {"message": "User answer saved"}

@app.route("/user_answers/<int:user_id>/<card_id>", methods=["GET"])
def get_user_answer(user_id, card_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT answer_text
        FROM user_answers
        WHERE user_id = %s
        AND card_id = %s
        """,
        (user_id, card_id)
    )

    answer = cursor.fetchone()

    cursor.close()
    conn.close()

    if answer:
        return {
            "answer": answer[0]
        }, 200

    return {
        "message": "No answer found"
    }, 404

if __name__ == "__main__":
    app.run(debug=True)