from flask import Flask, request, jsonify
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
    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (?, ?)",
            (email, password)
        )
    except sqlite3.IntegrityError:
        return {"message": "Email already registered"}, 400


    conn.commit()
    conn.close()
    return {
        "message": "User registered successfully"
        }

if __name__ == "__main__":
    app.run(debug=True)