#!/usr/bin/env python3
"""
Main entry point for the Navigation System application.

This script initializes and runs the Navigation System application with Web GUI.
No tkinter required - runs in your browser!
"""

import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

def main():
    """Main entry point"""
    try:
        from flask import Flask, render_template, request, jsonify
        import webbrowser
        from threading import Timer
        
        from src.backend.services.routing_service import RoutingService
        from src.backend.data_structures.trie import Trie
        
        # Initialize the app
        app = Flask(__name__, template_folder='.', static_folder='.')
        
        # Global services
        routing_service = None
        trie = None
        city_coordinates = {}
        
        # City coordinates (latitude, longitude)
        CITY_DATA = {
            "Paris": (48.8566, 2.3522),
            "London": (51.5074, -0.1278),
            "Tokyo": (35.6762, 139.6503),
            "Sydney": (-33.8688, 151.2093),
            "New York": (40.7128, -74.0060),
            "Berlin": (52.5200, 13.4050),
            "Barcelona": (41.3851, 2.1734),
            "Rome": (41.9028, 12.4964),
            "Amsterdam": (52.3676, 4.9041),
            "Dubai": (25.2048, 55.2708),
            "Madrid": (40.4168, -3.7038),
            "Vienna": (48.2082, 16.3738),
            "Prague": (50.0755, 14.4378),
            "Stockholm": (59.3293, 18.0686),
            "Athens": (37.9838, 23.7275),
            "Istanbul": (41.0082, 28.9784),
            "Moscow": (55.7558, 37.6173),
            "Bangkok": (13.7563, 100.5018),
            "Singapore": (1.3521, 103.8198),
            "Hong Kong": (22.3193, 114.1694),
            "Ukkadam": (11.0289, 76.9754),
            "Ettimadi": (11.1089, 76.2294),
            "Coimbatore": (11.0061, 76.9589),
            "Salem": (11.1461, 78.1581),
        }
        
        def initialize_services():
            """Initialize routing and trie services"""
            nonlocal routing_service, trie, city_coordinates
            
            print("Initializing Navigation System services...")
            
            # Initialize routing service
            routing_service = RoutingService()
            
            # Initialize Trie for search
            trie = Trie()
            city_coordinates = CITY_DATA.copy()
            
            for city in city_coordinates.keys():
                trie.insert(city)
            
            print(f"✓ Loaded {len(city_coordinates)} cities")
            print(f"✓ Navigation service initialized")
            return city_coordinates
        
        @app.route('/')
        def index():
            """Serve the main HTML page"""
            return render_template('map.html')
        
        @app.route('/api/cities', methods=['GET'])
        def get_all_cities():
            """Get all available cities with coordinates"""
            return jsonify({
                'cities': [
                    {'name': name, 'lat': coords[0], 'lng': coords[1]}
                    for name, coords in city_coordinates.items()
                ]
            })
        
        @app.route('/api/search', methods=['POST'])
        def search():
            """Search for cities by prefix"""
            data = request.json
            prefix = data.get('prefix', '').strip()
            
            if not prefix:
                return jsonify({'results': []})
            
            try:
                results = trie.search_prefix(prefix)
                return jsonify({'results': results})
            except Exception as e:
                return jsonify({'error': str(e)}), 400
        
        @app.route('/api/route', methods=['POST'])
        def calculate_route():
            """Calculate route between two cities"""
            data = request.json
            start = data.get('start', '').strip()
            end = data.get('end', '').strip()
            
            if not start or not end:
                return jsonify({'error': 'Start and end cities required'}), 400
            
            if start not in city_coordinates or end not in city_coordinates:
                return jsonify({'error': 'One or both cities not found'}), 400
            
            try:
                # For now, create a simple direct route between cities
                start_coords = city_coordinates[start]
                end_coords = city_coordinates[end]
                
                # Create a path with intermediate points
                distance = calculate_distance(start_coords, end_coords)
                
                return jsonify({
                    'success': True,
                    'start': start,
                    'end': end,
                    'start_coords': {'lat': start_coords[0], 'lng': start_coords[1]},
                    'end_coords': {'lat': end_coords[0], 'lng': end_coords[1]},
                    'distance': distance,
                    'waypoints': 2,
                    'coordinates': [
                        {'lat': start_coords[0], 'lng': start_coords[1]},
                        {'lat': end_coords[0], 'lng': end_coords[1]}
                    ]
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 400
        
        def calculate_distance(coords1, coords2):
            """Calculate distance between two coordinates using Haversine formula"""
            from math import radians, cos, sin, asin, sqrt
            
            lon1, lat1, lon2, lat2 = map(radians, [coords1[1], coords1[0], coords2[1], coords2[0]])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            km = 6371 * c
            return round(km, 2)
        
        def open_browser():
            """Open browser after a short delay"""
            Timer(1.5, lambda: webbrowser.open('http://localhost:8080')).start()
        
        # Initialize services
        initialize_services()
        
        print("\n" + "=" * 70)
        print("🚀 Navigation System - Web GUI with Map")
        print("=" * 70)
        print("\nOpening in browser: http://localhost:8080")
        print("\nPress Ctrl+C to stop the server")
        print("=" * 70 + "\n")
        
        # Open browser automatically
        open_browser()
        
        # Run Flask app
        app.run(debug=False, host='localhost', port=8080, use_reloader=False)
        
    except ImportError as e:
        print("\n" + "=" * 70)
        print("❌ ERROR: Missing required package")
        print("=" * 70)
        print(f"\nMissing: {e}")
        print("\nInstall Flask:")
        print("   pip install flask")
        print("\nOr use the CLI version:")
        print("   python cli.py")
        print("=" * 70 + "\n")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nShutting down gracefully...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
