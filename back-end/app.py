from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "IB Biology API running"}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect('ib_biology.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (email, hashed_password)
        )
    except sqlite3.IntegrityError:
        conn.close()
        return {"message": "Email already registered"}, 400

    conn.commit()
    conn.close()
    return {
        "message": "User registered successfully"
        }

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect('ib_biology.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, password_hash FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
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
    else:
        return {"message": "Invalid credentials"}, 401

@app.route("/review", methods=["POST"])
def save_review():
    data = request.get_json()

    user_id = data["user_id"]
    card_id = data["card_id"]

    conn = sqlite3.connect('ib_biology.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO review_cards (user_id, card_id)
            VALUES (?, ?)
            """,
            (user_id, card_id)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return {"message": "Card already marked"}, 400
    
    conn.close()
    return {"message": "Review card saved"}


@app.route("/review/<int:user_id>", methods=["GET"])
def get_review_cards(user_id):
    conn = sqlite3.connect("ib_biology.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT card_id
        FROM review_cards
        WHERE user_id = ?
        """,
        (user_id,)
    )

    cards = cursor.fetchall()
    conn.close()
    review_cards = [card[0] for card in cards]
    return {
        "review_cards": review_cards
    }

@app.route("/review/<int:user_id>/<card_id>", methods=["DELETE"])
def delete_review_card(user_id, card_id):

    conn = sqlite3.connect("ib_biology.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM review_cards
        WHERE user_id = ?
        AND card_id = ?
        """,
        (user_id, card_id)
    )

    conn.commit()
    conn.close()
    return {
        "message": "Review card removed"
    }

if __name__ == "__main__":
    app.run(debug=True)