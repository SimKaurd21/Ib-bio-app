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

    cursor.execute("SELECT password_hash FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return {"message": "Invalid credentials"}, 401

    stored_hash = user[0]
    if check_password_hash(stored_hash, password):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}, 401

if __name__ == "__main__":
    app.run(debug=True)