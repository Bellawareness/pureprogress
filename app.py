from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)
DB_NAME = 'habits.db'

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        data TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

init_db()

# Save daily habit data
@app.route('/habits', methods=['POST'])
def save_habit():
    payload = request.get_json()
    date = payload.get('date') or datetime.now().strftime('%Y-%m-%d')
    data = payload.get('data')
    if not data:
        return jsonify({'error': 'Missing habit data'}), 400
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM habits WHERE date = ?', (date,))
    c.execute('INSERT INTO habits (date, data) VALUES (?, ?)', (date, str(data)))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Saved', 'date': date})

# List all habit data
@app.route('/habits', methods=['GET'])
def list_habits():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT date, data FROM habits ORDER BY date DESC')
    rows = c.fetchall()
    conn.close()
    return jsonify([{'date': r[0], 'data': r[1]} for r in rows])

# Get a single day's habit data
@app.route('/habits/<date>', methods=['GET'])
def get_habit(date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT data FROM habits WHERE date = ?', (date,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify({'date': date, 'data': row[0]})
    return jsonify({'error': 'No data for this date'}), 404

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
