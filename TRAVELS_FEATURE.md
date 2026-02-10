# 🌍 Travel Tracking - Complete Guide

## Overview
A comprehensive travel tracking system to help you keep track of all the cities you've visited, no matter how long ago!

## Quick Start

### Add a City You Visited
1. Click the **🌍 Travels** tab
2. Fill in the **City Name** (required)
3. Add the **Country** (optional)
4. Select **When did you visit?** (month/year)
5. Write **Notes** about the place
6. Click **"Add City"**

### Find a City You Remember
- Use the search box at the top of the "Search & Filter" section
- Type the city name or country
- Results show instantly as you type

### Sort Your Travel List
Choose from the dropdown menu:
- **Most Recent** - Show newest visits first
- **Oldest First** - Show your earliest travels first  
- **Alphabetical (A-Z)** - Cities in A-Z order
- **By Country** - Group cities by country

### See Your Travel Stats
At the top of the Travels tab, you'll see:
- 🌐 **Total Cities Visited** - Count of unique cities
- 🗺️ **Total Countries** - How many countries you've been to

---

## What's New

### 1. **Database Table** (SQLite)
A new `cities` table with the following fields:
- `id` - Unique identifier
- `city_name` - Name of the city (required)
- `country` - Country name (optional)
- `date_visited` - Month/year you visited (stored as YYYY-MM format)
- `notes` - Your memories and notes about the place
- `added_date` - When you added this entry

### 2. **Backend API Endpoints** (Flask)
New REST API endpoints for managing cities:

#### POST `/cities`
Add a new city to your travels
```json
{
  "city_name": "Paris",
  "country": "France",
  "date_visited": "2023-06",
  "notes": "Beautiful architecture and amazing food"
}
```

#### GET `/cities`
Retrieve all cities (sorted by most recent visit date)
```json
[
  {
    "id": 1,
    "city_name": "Paris",
    "country": "France",
    "date_visited": "2023-06",
    "notes": "...",
    "added_date": "2025-12-12"
  }
]
```

#### GET `/cities/<id>`
Get a specific city

#### PUT `/cities/<id>`
Update a city's information

#### DELETE `/cities/<id>`
Remove a city from your travels

#### GET `/cities/stats`
Get travel statistics (total cities and countries)

### 3. **User Interface**

#### New "🌍 Travels" Tab
- Added to the main navigation alongside Today and History
- Click to view your complete travel journal

#### Travel Statistics Section
- **Cities Visited**: Total count of unique cities
- **Countries**: Total count of unique countries (for motivation!)

#### Add City Form
Easy-to-use form to add new cities:
- City Name (required) - e.g., "Paris", "Tokyo", "New York"
- Country (optional) - e.g., "France", "Japan", "USA"
- When did you visit? (optional) - Month/Year picker
- Notes (optional) - Remember your favorite food, memorable moments, etc.

#### Search & Filter
- **Search Bar**: Find cities by name, country, or keywords in notes
- **Sort Options**:
  - Most Recent (default)
  - Oldest First
  - Alphabetical (A-Z)
  - By Country

#### City Cards Display
Beautiful card layout showing:
- City name and country (prominent display)
- Date visited (formatted nicely, e.g., "June 2023")
- Your notes about the city
- Date when you added this entry
- Delete button for each city

### 4. **Key Features**

✅ **Long-term tracking** - Store cities from years ago with month/year precision
✅ **Searchable** - Quickly find any city you've visited
✅ **Sortable** - View by recent, oldest, alphabetically, or by country
✅ **Notes storage** - Remember what made each place special
✅ **Statistics** - See how many cities and countries you've visited
✅ **Clean UI** - Beautiful, intuitive interface that matches your habit tracker theme
✅ **Responsive** - Works on desktop, tablet, and mobile

## How to Use

### Adding Your First City
1. Click the **🌍 Travels** tab
2. Scroll to "✈️ Add a City"
3. Enter city name (required)
4. Add country and visit date (optional but recommended)
5. Add notes about your experience
6. Click "Add City"

### Finding a City
1. Use the search bar to type a city name or country
2. Results update instantly as you type

### Organizing Your List
1. Use the "Sort" dropdown to reorder cities
2. View by most recent visits, alphabetically, or grouped by country

### Remembering Details
Each city card shows:
- When you visited (formatted date)
- Your personal notes about the place
- When you added the entry

## Technical Details

### Database Schema
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

### Files Modified
- `app.py` - Added database migration and REST API endpoints
- `templates/index.html` - Added UI, new tab, and JavaScript functions

### JavaScript Functions
- `loadTravels()` - Load and initialize travels view
- `addCity()` - Add a new city
- `fetchCities()` - Get cities from server
- `filterAndSortCities()` - Search and sort functionality
- `displayCities()` - Render city cards
- `deleteCity()` - Remove a city
- `updateTravelStats()` - Update statistics
- `formatDateVisited()` - Format dates nicely
- `formatAddedDate()` - Show relative dates (e.g., "2 days ago")

## Future Enhancement Ideas
- 📷 Add photos to each city
- 📍 Add GPS coordinates/map integration
- 🎯 Create travel goals (e.g., "Visit 50 cities")
- 📊 Travel timeline visualization
- 🏆 Achievement badges (e.g., "5 Countries", "50 Cities")
- 📤 Export travel list as PDF or CSV
- 🌐 Rate cities (1-5 stars)
- 🗺️ Interactive map showing all visited cities

## Tips for Using

1. **Add from memory** - It's okay to not remember exact dates. Just add the month/year or year you visited.
2. **Be detailed in notes** - These notes help you remember special moments years later.
3. **Search regularly** - As your list grows, searching helps you find cities quickly.
4. **Sort by country** - Great way to see how many cities you've visited in each country!
5. **Keep it organized** - Regular updates help you maintain an accurate travel journal.

---

Enjoy tracking your travels! 🌍✈️
