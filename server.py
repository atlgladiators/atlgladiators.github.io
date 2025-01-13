from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS players (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        dob TEXT NOT NULL,
                        position TEXT NOT NULL,
                        experience INTEGER NOT NULL
                    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['POST'])
def register_player():
    data = request.form
    full_name = data.get('fullName')
    email = data.get('email')
    phone = data.get('phone')
    dob = data.get('dob')
    position = data.get('position')
    experience = data.get('experience')

    conn = sqlite3.connect('players.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO players (full_name, email, phone, dob, position, experience)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (full_name, email, phone, dob, position, experience))
    conn.commit()
    conn.close()

    return jsonify({"message": "Player registered successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
