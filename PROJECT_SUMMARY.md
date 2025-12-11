# 🗺️ Navigation System - Project Summary

## Overview

A modern web-based navigation system built with Flask and Leaflet.js that allows users to search for cities and calculate routes with visual map display.

## ✨ Features

### Core Functionality

- **Interactive Map**: Real-time map visualization using Leaflet.js with OpenStreetMap tiles
- **City Search**: Fast prefix-based city search using Trie data structure
- **Route Calculation**: Calculate distances between any two cities
- **Visual Routes**: Display routes on the interactive map with start/end markers
- **Responsive Design**: Mobile-friendly interface that adapts to different screen sizes

### Available Cities

- **International**: Paris, London, Tokyo, Sydney, New York, Berlin, Barcelona, Rome, Amsterdam, Dubai, Madrid, Vienna, Prague, Stockholm, Athens, Istanbul, Moscow, Bangkok, Singapore, Hong Kong
- **India (Tamil Nadu)**: Coimbatore, Salem, Ukkadam, Ettimadi

## 🏗️ Architecture

### Backend (Flask)

- **Framework**: Flask
- **Port**: 8080
- **Main File**: `main.py`

#### API Endpoints

- `GET /` - Serves the interactive map HTML
- `GET /api/cities` - Returns all available cities with coordinates
- `POST /api/search` - Search cities by prefix
- `POST /api/route` - Calculate route between two cities

### Frontend (HTML/CSS/JavaScript)

- **Map Library**: Leaflet.js v1.9.4
- **Routing Library**: Leaflet Routing Machine v3.2.12
- **Styling**: Custom CSS with responsive design
- **Main File**: `map.html`

### Data Structures

- **Trie**: Fast prefix-based city search
- **Location Dictionary**: City names mapped to (latitude, longitude) coordinates

## 📁 Project Structure

```
NavigationSystem/
├── main.py                 # Flask application entry point
├── map.html               # Interactive map UI (template)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── PROJECT_SUMMARY.md     # This file
├── cli.py                 # Command-line interface version
├── config/                # Configuration module
│   ├── __init__.py
│   └── settings.py
├── src/                   # Source code
│   ├── __init__.py
│   ├── app.py            # Legacy tkinter app
│   ├── backend/          # Backend services
│   │   ├── algorithms/   # Pathfinding algorithms
│   │   ├── data_structures/  # Trie and N-ary tree
│   │   └── services/     # Routing service
│   └── frontend/         # Frontend components
│       ├── ui/           # UI panels
│       └── styles/       # Styling
├── .venv/                # Python virtual environment
└── cache/                # Cached data
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Virtual environment (venv)

### Installation

1. **Navigate to project directory**

   ```bash
   cd /Users/praneethudayakumar227/Documents/GitHub/NavigationSystem
   ```

2. **Activate virtual environment**

   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

### Running the Application

**Start the Flask server:**

```bash
python main.py
```

The application will:

- Initialize the routing and search services
- Load 24 cities into the system
- Open your browser automatically to `http://localhost:8080`
- Display the interactive map with search and routing features

**Stop the server:**

- Press `Ctrl+C` in the terminal

## 💻 Usage Guide

### Search for a City

1. Type a city name (or prefix) in the "Find a City" field
2. Select from autocomplete suggestions or click "Pin City"
3. The city will be marked on the map

### Calculate a Route

1. Enter a starting city in the "From" field
2. Enter a destination city in the "To" field
3. Click "Calculate Route"
4. The route will be drawn on the map with distance displayed
5. Click "Clear Route" to remove the visualization

### Map Interaction

- **Zoom**: Scroll wheel or pinch gesture
- **Pan**: Click and drag
- **View Route**: Map automatically fits to show the entire route

## 🛠️ Technical Details

### Distance Calculation

- Uses Haversine formula for great-circle distance
- Returns distance in kilometers

### Search Implementation

- **Trie Data Structure**: O(n) search where n is the length of prefix
- Autocomplete provides real-time suggestions

### Route Visualization

- Uses Leaflet Routing Machine for visual path drawing
- Green marker for start point
- Red marker for destination
- Blue route line connecting both points

## 📦 Dependencies

### Core

- **flask**: Web framework for HTTP endpoints
- **python 3.9+**: Base runtime

### Frontend (CDN)

- **Leaflet.js**: Interactive mapping library
- **Leaflet Routing Machine**: Route visualization
- **OpenStreetMap**: Tile provider

## 🔧 Configuration

### City Data

Cities are stored in `CITY_DATA` dictionary in `main.py`:

```python
CITY_DATA = {
    "CityName": (latitude, longitude),
    ...
}
```

### Server Configuration

- **Host**: localhost
- **Port**: 8080
- **Debug Mode**: Off (for production)
- **Auto Reload**: Disabled

## 📝 Key Files

| File                                      | Purpose                          |
| ----------------------------------------- | -------------------------------- |
| `main.py`                                 | Flask app with all API endpoints |
| `map.html`                                | Interactive map UI with Leaflet  |
| `requirements.txt`                        | Python package dependencies      |
| `src/backend/data_structures/trie.py`     | Trie implementation for search   |
| `src/backend/algorithms/pathfinding.py`   | Pathfinding algorithms           |
| `src/backend/services/routing_service.py` | Route calculation service        |

## ✅ Testing

### Manual Testing

Open `http://localhost:8080` and:

1. ✅ Search for cities (e.g., "Par" → "Paris")
2. ✅ Calculate routes (e.g., Paris → London)
3. ✅ Verify distance calculations
4. ✅ Test mobile responsiveness

### API Endpoints (via curl)

```bash
# Get all cities
curl http://localhost:8080/api/cities

# Search cities
curl -X POST http://localhost:8080/api/search \
  -H "Content-Type: application/json" \
  -d '{"prefix":"Par"}'

# Calculate route
curl -X POST http://localhost:8080/api/route \
  -H "Content-Type: application/json" \
  -d '{"start":"Paris","end":"London"}'
```

## 🎯 Future Enhancements

Potential improvements for future versions:

- Real-time turn-by-turn directions
- Multiple route options (shortest, fastest, scenic)
- Traffic and road condition data
- Offline map support
- User authentication and saved routes
- Dark mode theme
- Multi-language support
- Advanced filtering options
- Database integration for persistence

## 📄 License

This project is part of the NavigationSystem repository.

## 👤 Author

Created as a navigation system demonstration with Flask and Leaflet.js mapping.

---

**Last Updated**: December 11, 2025
**Status**: ✅ Fully Functional
