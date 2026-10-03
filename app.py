from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask("champ_motel")
CORS(app)

DATABASE = "motel.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            check_in TEXT NOT NULL,
            check_out TEXT NOT NULL,
            room_type TEXT NOT NULL,
            guests INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return jsonify({
        "message": "Champ Motel Backend is running!",
        "status": "success"
    })


@app.route("/api/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()

    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        INSERT INTO bookings
        (name, email, check_in, check_out, room_type, guests)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["email"],
        data["check_in"],
        data["check_out"],
        data["room_type"],
        data["guests"]
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Booking saved successfully!",
        "status": "success"
    }), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
