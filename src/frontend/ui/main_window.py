"""Main window component for the application"""

import tkinter as tk
from src.frontend.ui.search_panel import SearchPanel
from src.frontend.ui.map_panel import MapPanel
from src.frontend.ui.directions_panel import DirectionsPanel


class MainWindow:
    """
    Main application window that coordinates all UI components.
    """

    def __init__(self, root, on_search_callback):
        """
        Initialize the main window.

        Args:
            root: Root tkinter widget
            on_search_callback: Callback function when search is performed
        """
        self.root = root
        self.root.title("Navigation Map")
        self.root.geometry("1000x900")
        self.root.configure(bg='#f0f0f0')

        # Create UI panels
        self.search_panel = SearchPanel(self.root, on_search_callback)
        self.map_panel = MapPanel(self.root)
        self.directions_panel = DirectionsPanel(self.root)

        # Initialize panels
        self.search_panel.create()
        self.map_panel.create()
        self.directions_panel.create()

    def update_suggestions(self, suggestions):
        """Update location suggestions"""
        self.search_panel.update_suggestions(suggestions)

    def get_search_locations(self):
        """Get the current search locations"""
        return self.search_panel.get_locations()

    def get_active_entry(self):
        """Get which entry field is currently active"""
        return self.search_panel.active_entry

    def display_route(self, route_coordinates, start_label="Start", end_label="End"):
        """Display a route on the map"""
        self.map_panel.display_route(route_coordinates, start_label, end_label)

    def display_directions(self, start_location, end_location, directions, distance=None):
        """Display directions in the directions panel"""
        self.directions_panel.display_directions(start_location, end_location, directions, distance)

    def display_error(self, error_message):
        """Display an error message"""
        self.directions_panel.display_error(error_message)

    def clear_route(self):
        """Clear the route from the map"""
        self.map_panel.clear_route()

    def center_on_location(self, lat, lon, zoom=15):
        """Center the map on a location"""
        self.map_panel.center_on_location(lat, lon, zoom)

    def run(self):
        """Start the main event loop"""
        self.root.mainloop()
