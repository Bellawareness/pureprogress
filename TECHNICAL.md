# Technical Documentation - Backend & API

A Flask backend for the Learn Thyself habit tracker frontend. Provides endpoints to save and load daily habit data and is designed to integrate with the frontend.

## Features

- Save daily habit data (POST /habits)
- List all saved days (GET /habits)
- Get a single day's data (GET /habits/<date>)
- Travel tracking endpoints (GET/POST/PUT/DELETE /cities)
- Uses SQLite for storage
- CORS enabled for frontend integration
- Responsive design with full frontend feature support

### Frontend Features Supported
- Weekly matrix (7-day view) of activities
- Per-activity streaks
- Daily Ratings (mood / energy sliders, 0–100)
- Mood / energy notes (saved with the day)
- Custom activities (created/deleted in UI)
- Daily To Do / Get It Done lists
- Language toggle (English / Español)
- Accessibility & reduced-motion support
- Travel tracking (cities, countries, visit dates)

---

## Quick Start

### 1. Setup Environment

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Server

Start the Flask app (defaults to port 5000):

```bash
python3 app.py
```

Or use Flask CLI:

```bash
export FLASK_APP=app.py
flask run
```

### 3. Open the Frontend

Choose one of these options:

**Option A — Direct Open (file://):**
```bash
open /Users/elysian/Downloads/Organize/habittracker/templates/index.html
```

**Option B — Local HTTP Server (Recommended):**
```bash
cd /Users/elysian/Downloads/Organize/habittracker
python3 -m http.server 8001
# Then open: http://localhost:8001/templates/index.html
```

**Option C — VS Code Live Server:**
- Right-click `index.html` in VS Code
- Select "Open with Live Server"

---

## API Reference

**Base URL:** `http://localhost:5000`

### Habits Endpoints

#### GET /habits
Returns an array of all saved days:
```json
[
  {
    "date": "2025-10-28",
    "data": {
      "Spanish": true,
      "mood": 4,
      "moodNote": "Felt focused",
      "relationship": 72,
      "activities": ["Workout", "Reading"],
      "spending": 25.50,
      "notes": "Great day!"
    }
  }
]
```

#### GET /habits/<date>
Get data for a specific date:
```
GET /habits/2025-10-28
```

Returns the object for that date or 404 if not found.

#### POST /habits
Save data for a date:
```bash
curl -X POST http://localhost:5000/habits \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2025-10-29",
    "data": {
      "Spanish": true,
      "Code": false,
      "mood": 4,
      "moodNote": "Felt focused",
      "relationship": 85
    }
  }'
```

**Request JSON:**
```json
{
  "date": "YYYY-MM-DD",
  "data": {
    "mood": 1-5,
    "moodNote": "string",
    "energy": 1-5,
    "energyNote": "string",
    "relationship": 0-100,
    "health": 0-100,
    "money": 0-100,
    "learning": 0-100,
    "fun": 0-100,
    "activities": ["activity1", "activity2"],
    "spending": number,
    "sleep": number,
    "water": number,
    "pain": number,
    "clarity": number
  }
}
```

The `data` object can contain any additional fields - they will be stored as provided.

---

### Travel/Cities Endpoints

#### GET /cities
Retrieve all cities (sorted by most recent visit date):
```json
[
  {
    "id": 1,
    "city_name": "Paris",
    "country": "France",
    "date_visited": "2023-06",
    "notes": "Beautiful architecture and amazing food",
    "added_date": "2025-12-12"
  }
]
```

#### GET /cities/<id>
Get a specific city:
```
GET /cities/1
```

#### GET /cities/stats
Get travel statistics (total cities and countries):
```json
{
  "total_cities": 15,
  "total_countries": 8
}
```

#### POST /cities
Add a new city:
```bash
curl -X POST http://localhost:5000/cities \
  -H "Content-Type: application/json" \
  -d '{
    "city_name": "Tokyo",
    "country": "Japan",
    "date_visited": "2024-03",
    "notes": "Incredible food and technology"
  }'
```

**Request JSON:**
```json
{
  "city_name": "City Name (required)",
  "country": "Country (optional)",
  "date_visited": "YYYY-MM format (optional)",
  "notes": "Your notes (optional)"
}
```

#### PUT /cities/<id>
Update a city:
```bash
curl -X PUT http://localhost:5000/cities/1 \
  -H "Content-Type: application/json" \
  -d '{
    "city_name": "Paris",
    "country": "France",
    "date_visited": "2023-06",
    "notes": "Updated notes about the city"
  }'
```

#### DELETE /cities/<id>
Remove a city:
```bash
curl -X DELETE http://localhost:5000/cities/1
```

---

## Database Schema

### Habits Table
```sql
CREATE TABLE habits (
  id INTEGER PRIMARY KEY,
  date TEXT UNIQUE NOT NULL,
  data TEXT NOT NULL,
  created_at TEXT,
  updated_at TEXT
)
```

### Cities Table
```sql
CREATE TABLE cities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city_name TEXT NOT NULL,
  country TEXT,
  date_visited TEXT,
  notes TEXT,
  added_date TEXT NOT NULL
)
```

---

## Data Storage Notes

### Server-side
- Days are persisted in SQLite
- Backend accepts and stores the JSON `data` object for each date
- All data survives server restarts

### Client-side
- Custom activity list stored in localStorage (per-browser)
- To Do / Get It Done lists stored in localStorage
- Mood and energy notes saved in the day's `data`
- Firebase sync handles cross-device synchronization

---

## Optional Improvements

- **Persist Lists on Backend**: Add endpoints to sync custom activities and to-do lists across devices
- **Authentication**: Add user authentication for per-user storage
- **Export**: Add CSV export endpoints for data analysis
- **Backup**: Add automated backup endpoints

---

## Troubleshooting

### Saved data doesn't appear in the app
1. Ensure the frontend POST to `/habits` returns HTTP 200
2. Check browser DevTools → Network for response status
3. Ensure the GET /habits response contains the expected fields

### Buttons don't register clicks
1. Confirm no overlay element is covering UI (use DevTools Element inspector)
2. Try running the frontend from a local HTTP server instead of file://

### Cities don't appear
1. Check that POST /cities returned 200 status
2. Verify Firefox/Chrome DevTools → Network shows successful request
3. Try refreshing the page

### CORS errors in console
- CORS is already enabled in app.py
- Make sure you're accessing via http://localhost, not file://
- Check that Flask is running on port 5000

---

## Development

To extend the API:
1. Edit `app.py` to add new endpoints
2. Modify `templates/index.html` frontend to call new endpoints
3. Update database schema if needed (add migrations)
4. Test with curl or Postman before frontend integration

Remember to activate the virtualenv before installing or running commands:
```bash
source .venv/bin/activate
```

---

## Example Workflows

### Save Today's Mood
```bash
curl -X POST http://localhost:5000/habits \
  -H "Content-Type: application/json" \
  -d '{
    "date": "'$(date +%Y-%m-%d)'",
    "data": {
      "mood": 4,
      "moodNote": "Great day!",
      "energy": 4
    }
  }'
```

### Get Last 7 Days
```bash
curl http://localhost:5000/habits | jq '.[-7:]'
```

### List All Cities Visited
```bash
curl http://localhost:5000/cities | jq '.'
```

### Add a Travel Memory
```bash
curl -X POST http://localhost:5000/cities \
  -H "Content-Type: application/json" \
  -d '{
    "city_name": "Barcelona",
    "country": "Spain",
    "date_visited": "2022-07",
    "notes": "Beach, architecture, and delicious tapas"
  }'
```

---

**Need Help?** Check app.py for implementation details and browser console (F12) for error messages.
