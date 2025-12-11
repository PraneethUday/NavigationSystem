# Navigation System

A professional-grade navigation and route planning application built with Python and Tkinter.

## Features

- **Interactive Map Display**: Real-time map visualization using TkinterMapView
- **Route Planning**: Find optimal routes between locations using OpenStreetMap data
- **Location Search**: Autocomplete suggestions for location search using Trie data structure
- **Turn-by-Turn Directions**: Detailed directions with coordinates
- **Distance Calculation**: Get total route distance in kilometers
- **Professional Architecture**: Clean separation of frontend and backend components

## Project Structure

```
NavigationSystem/
├── src/
│   ├── backend/                 # Backend business logic
│   │   ├── data_structures/    # Trie and N-ary tree implementations
│   │   ├── algorithms/         # Pathfinding algorithms
│   │   └── services/           # Routing service
│   ├── frontend/                # Frontend UI components
│   │   ├── ui/                 # UI panels and main window
│   │   └── styles/             # Theme and styling
│   └── app.py                  # Main application coordinator
├── config/                      # Configuration settings
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:

```bash
git clone <repository-url>
cd NavigationSystem
```

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

### How to Use

1. **Enter Start Location**: Type or select a location in the "Current Location" field
2. **Enter Destination**: Type or select a location in the "Destination" field
3. **Get Directions**: Click the "Get Directions" button
4. **View Results**:
   - The map will display the calculated route in blue
   - Start and end markers will appear on the map
   - Detailed turn-by-turn directions and distance will be shown

## Architecture

### Backend Components

#### Data Structures

- **Trie**: For efficient location search and autocomplete suggestions
- **N-ary Tree**: For hierarchical organization of locations

#### Algorithms

- **Pathfinding**: Uses NetworkX's shortest path algorithm (Dijkstra)
- Supports weighted graphs for realistic route optimization

#### Services

- **RoutingService**: Handles all routing-related operations
  - Geocoding (location name to coordinates)
  - Road network graph creation
  - Shortest path calculation
  - Direction generation

### Frontend Components

#### UI Panels

- **SearchPanel**: Location input and autocomplete
- **MapPanel**: Interactive map display
- **DirectionsPanel**: Route information and directions

#### Styling

- Consistent color scheme
- Professional typography
- Responsive layout

## Configuration

Edit `config/settings.py` to customize:

- Default map location and zoom level
- Graph distance for road networks
- Network type ('drive', 'walk', 'bike')
- UI window size
- Maximum number of suggestions

## Error Handling

The application includes comprehensive error handling for:

- Invalid location names
- Network connectivity issues
- Missing paths between locations
- Invalid coordinates

## Dependencies

- **tkinter**: GUI framework (included with Python)
- **tkintermapview**: Interactive map widget
- **osmnx**: OpenStreetMap data retrieval and routing
- **networkx**: Graph algorithms and data structures

## Performance

- **Location Search**: O(m) where m is the length of the search term (Trie)
- **Pathfinding**: O((V + E) log V) using Dijkstra's algorithm
- **Map Rendering**: Real-time updates for routes and markers

## Future Enhancements

- [ ] Multiple route alternatives
- [ ] Traffic-aware routing
- [ ] User preferences (fastest, shortest, safest)
- [ ] Route saving and history
- [ ] Real-time traffic data
- [ ] Voice turn-by-turn guidance
- [ ] Mobile app version
- [ ] Web interface

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please create an issue in the repository.

## Authors

[Add author information here]
Developed an interactive map-based navigation system with auto-suggestion for locations using Trie and hierarchical N-ary tree structure for spatial data management.
