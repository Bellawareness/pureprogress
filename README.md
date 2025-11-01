# Habit Tracker — Flask Backend

A Flask backend for the Learn Thyself habit tracker frontend. Provides endpoints to save and load daily habit data and is designed to integrate with the frontend served from the repository.

## Features
- Save daily habit data (POST /habits)
- List all saved days (GET /habits)
- Get a single day's data (GET /habits/<date>)
- Uses SQLite for storage
- CORS enabled for frontend integration
- Frontend features supported:
  - Weekly matrix (7-day view) of activities
  - Per-activity streaks
  - Daily Ratings (mood / energy sliders, 0–100)
  - Mood / energy notes (saved with the day)
  - Custom activities (created/deleted in UI; stored in localStorage by default)
  - Daily To Do / Get It Done lists (stored in localStorage by default)
  - Language toggle (English / Español)
  - Accessibility & reduced-motion support

## Quick start

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Start the Flask app (defaults to port 5000):
   ```bash
   python3 app.py
   ```
   or
   ```bash
   export FLASK_APP=app.py
   flask run
   ```

3. Open the frontend:
   - Option A — quick open (static file): open `habittracker/templates/index.html` in your browser (works for simple checks).
   - Option B — local static server (recommended):
     ```bash
     cd /Users/elysian/Downloads/Organize/habittracker
     python3 -m http.server 8001
     # open http://localhost:8001/templates/index.html
     ```
   - Option C — VS Code Live Server: right-click the file and "Open with Live Server".

## API

Base URL: http://localhost:5000

- GET /habits
  - Returns an array of saved day objects:
    ```json
    [
      { "date": "2025-10-28", "data": { "Spanish": true, "mood": 4, "moodNote": "...", "relationship": 72, ... } },
      ...
    ]
    ```

- GET /habits/<date>
  - Example:
    ```
    GET /habits/2025-10-28
    ```
  - Returns the object for that date or 404.

- POST /habits
  - Request JSON: `{ "date": "YYYY-MM-DD", "data": { ... } }`
  - The `data` object can contain:
    - boolean activity keys (e.g., "Spanish": true)
    - slider ratings (relationship, health, money, learning, fun) as integers 0–100
    - mood (1–5), energy (1–5)
    - moodNote, energyNote (strings)
    - any additional fields — they will be stored as provided
  - Example:
    ```bash
    curl -X POST http://localhost:5000/habits \
      -H "Content-Type: application/json" \
      -d '{"date":"2025-10-29","data":{"Spanish":true,"Code":false,"mood":4,"moodNote":"Felt focused","relationship":85}}'
    ```

## Data storage notes
- Server-side: days are persisted in SQLite. The backend accepts and stores the JSON `data` object for each date.
- Client-side:
  - Custom activity list and To Do / Get It Done lists are stored in localStorage (per-browser). If you want cross-device sync, enable server-side persistence (see next section).
  - Mood and energy notes are saved in the day's `data` and will appear in the weekly review.

## Optional improvements / integration points
- Persist custom activities and to-do lists on the backend to sync across devices (requires adding endpoints and small client changes).
- Add authentication if you want per-user storage.
- Add export (CSV) or backup endpoints.

## Troubleshooting
- If saved mood/energy notes don't appear in the weekly view:
  - Ensure the frontend POST to `/habits` returns HTTP 200 (check browser DevTools → Network).
  - Ensure the GET /habits response contains the `moodNote` / `energyNote` fields (backend stores whatever `data` you send).
- If buttons don't register clicks:
  - Confirm no overlay element is covering UI (use DevTools Element inspector).
  - Try running the frontend from a local HTTP server (python -m http.server) instead of file:// for consistent behavior.

## Development
- To run tests or extend the API, edit `app.py` and the templates in `habittracker/templates/`.
- Remember to activate the virtualenv before installing or running commands.

---

If you want, I can:
- Add server endpoints to persist custom activities and to-do lists.
- Add example Postman collection or curl scripts for common tasks.
