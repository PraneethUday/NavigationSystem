#!/usr/bin/env python3
"""
CLI entry point for the Navigation System application.

This version runs without GUI - useful for testing and server environments.
For the GUI version on macOS, ensure tkinter is properly installed.
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(__file__))

from src.backend.data_structures import Trie
from src.backend.services import RoutingService


def main_cli():
    """Main CLI entry point"""
    print("\n" + "=" * 60)
    print("Navigation System - CLI Mode")
    print("=" * 60)
    
    # Initialize services
    routing_service = RoutingService()
    location_trie = Trie()
    
    # Populate with sample cities
    cities = [
        "Paris", "London", "New York", "Tokyo", "Sydney",
        "Dubai", "Singapore", "Bangkok", "Mumbai", "Toronto"
    ]
    
    for city in cities:
        location_trie.insert(city)
    
    print(f"\n✓ Loaded {len(cities)} sample cities")
    print("✓ Navigation service initialized")
    
    print("\n" + "-" * 60)
    print("Available Commands:")
    print("-" * 60)
    print("  1. search <prefix>     - Search for cities by prefix")
    print("  2. route <from> <to>   - Calculate route between cities")
    print("  3. cities              - List all available cities")
    print("  4. help                - Show this help message")
    print("  5. exit                - Exit the application")
    print("-" * 60 + "\n")
    
    while True:
        try:
            command = input("> ").strip()
            
            if not command:
                continue
            
            parts = command.split(maxsplit=2)
            action = parts[0].lower()
            
            if action == "exit" or action == "quit":
                print("\nGoodbye!")
                break
            
            elif action == "help":
                print("\n" + "-" * 60)
                print("Available Commands:")
                print("-" * 60)
                print("  search <prefix>     - Search for cities by prefix")
                print("  route <from> <to>   - Calculate route between cities")
                print("  cities              - List all available cities")
                print("  help                - Show this help message")
                print("  exit                - Exit the application")
                print("-" * 60 + "\n")
            
            elif action == "search":
                if len(parts) < 2:
                    print("Usage: search <prefix>")
                    continue
                
                prefix = parts[1]
                results = location_trie.search_prefix(prefix)
                
                if results:
                    print(f"\n✓ Found {len(results)} cities matching '{prefix}':")
                    for city in results:
                        print(f"  - {city}")
                else:
                    print(f"\n✗ No cities found matching '{prefix}'")
                print()
            
            elif action == "cities":
                print("\nAvailable cities:")
                for city in cities:
                    print(f"  - {city}")
                print()
            
            elif action == "route":
                if len(parts) < 3:
                    print("Usage: route <from_city> <to_city>")
                    continue
                
                from_city = parts[1]
                to_city = parts[2]
                
                print(f"\nCalculating route from {from_city} to {to_city}...")
                
                try:
                    route_data = routing_service.calculate_route(from_city, to_city)
                    
                    print(f"\n✓ Route calculated successfully!")
                    print(f"  Start: {from_city}")
                    print(f"  End: {to_city}")
                    
                    distance_km = route_data['distance'] / 1000
                    print(f"  Distance: {distance_km:.2f} km")
                    print(f"  Way points: {len(route_data['coordinates'])} points")
                    
                    directions = routing_service.get_turn_by_turn_directions(
                        route_data['coordinates']
                    )
                    
                    print(f"\n  First 5 directions:")
                    for i, direction in enumerate(directions[:5], 1):
                        print(f"    {i}. {direction}")
                    
                    if len(directions) > 5:
                        print(f"    ... and {len(directions) - 5} more")
                    print()
                
                except ValueError as e:
                    print(f"\n✗ Error: {e}\n")
                except RuntimeError as e:
                    print(f"\n✗ Error: {e}\n")
            
            else:
                print(f"Unknown command: {action}")
                print("Type 'help' for available commands.\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\n✗ Error: {e}\n")


if __name__ == "__main__":
    main_cli()
