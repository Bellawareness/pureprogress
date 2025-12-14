from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from datetime import datetime
import os, time

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
CORS(app, resources={r"/*": {"origins": "*"}})
DB_NAME = 'habits.db'

# Simple cache-busting version for static files
ASSET_VER = os.getenv('ASSET_VER', str(int(time.time())))

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        data TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT NOT NULL,
        country TEXT,
        date_visited TEXT,
        notes TEXT,
        added_date TEXT NOT NULL
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

# Cities/Travels API
@app.route('/cities/stats', methods=['GET'])
def get_cities_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM cities')
    total_cities = c.fetchone()[0]
    c.execute('SELECT COUNT(DISTINCT country) FROM cities WHERE country IS NOT NULL AND country != ""')
    total_countries = c.fetchone()[0]
    conn.close()
    return jsonify({'total_cities': total_cities, 'total_countries': total_countries})

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, city_name, country, date_visited, notes, added_date FROM cities WHERE id = ?', (city_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify({
            'id': row[0],
            'city_name': row[1],
            'country': row[2],
            'date_visited': row[3],
            'notes': row[4],
            'added_date': row[5]
        })
    return jsonify({'error': 'City not found'}), 404

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    payload = request.get_json()
    city_name = payload.get('city_name', '').strip()
    country = payload.get('country', '').strip()
    date_visited = payload.get('date_visited', '').strip()
    notes = payload.get('notes', '').strip()
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''UPDATE cities SET city_name=?, country=?, date_visited=?, notes=? WHERE id=?''',
              (city_name, country, date_visited, notes, city_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'City updated'})

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM cities WHERE id = ?', (city_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'City deleted'})

@app.route('/cities', methods=['POST'])
def add_city():
    payload = request.get_json()
    city_name = payload.get('city_name', '').strip()
    country = payload.get('country', '').strip()
    date_visited = payload.get('date_visited', '').strip()
    notes = payload.get('notes', '').strip()
    
    if not city_name:
        return jsonify({'error': 'City name is required'}), 400
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    added_date = datetime.now().strftime('%Y-%m-%d')
    c.execute('''INSERT INTO cities (city_name, country, date_visited, notes, added_date)
                VALUES (?, ?, ?, ?, ?)''',
              (city_name, country, date_visited, notes, added_date))
    conn.commit()
    city_id = c.lastrowid
    conn.close()
    return jsonify({'message': 'City added', 'id': city_id}), 201

@app.route('/cities', methods=['GET'])
def list_cities():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''SELECT id, city_name, country, date_visited, notes, added_date 
                FROM cities ORDER BY date_visited DESC, added_date DESC''')
    rows = c.fetchall()
    conn.close()
    cities = []
    for row in rows:
        cities.append({
            'id': row[0],
            'city_name': row[1],
            'country': row[2],
            'date_visited': row[3],
            'notes': row[4],
            'added_date': row[5]
        })
    return jsonify(cities)

@app.route('/')
def home():
    return render_template('index.html', asset_version=ASSET_VER)

if __name__ == '__main__':
    app.run(debug=True)
