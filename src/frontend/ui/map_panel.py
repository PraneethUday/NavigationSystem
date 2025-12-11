"""Map panel component for displaying the interactive map"""

from tkintermapview import TkinterMapView


class MapPanel:
    """
    Panel for displaying the interactive map and route visualization.
    """

    def __init__(self, parent):
        """
        Initialize the map panel.

        Args:
            parent: Parent tkinter widget
        """
        self.parent = parent
        self.map_widget = None
        self.current_route_path = None

    def create(self):
        """Create and layout the map panel"""
        self.map_widget = TkinterMapView(self.parent, width=800, height=500, corner_radius=10)
        self.map_widget.pack(pady=10)
        self.set_initial_position()

    def set_initial_position(self, lat=48.860381, lon=2.338594, zoom=15):
        """
        Set the initial map position and zoom level.

        Args:
            lat (float): Latitude (default: Paris)
            lon (float): Longitude (default: Paris)
            zoom (int): Zoom level
        """
        self.map_widget.set_position(lat, lon)
        self.map_widget.set_zoom(zoom)

    def display_route(self, route_coordinates, start_label="Start", end_label="End"):
        """
        Display a route on the map.

        Args:
            route_coordinates (list): List of (lat, lon) tuples
            start_label (str): Label for the start marker
            end_label (str): Label for the end marker
        """
        if not route_coordinates:
            return

        # Remove previous route if exists
        if self.current_route_path:
            self.map_widget.delete(self.current_route_path)

        # Draw route
        self.current_route_path = self.map_widget.set_path(route_coordinates, color="blue", width=2)

        # Set map position to start of route
        self.map_widget.set_position(route_coordinates[0][0], route_coordinates[0][1])
        self.map_widget.set_zoom(12)

        # Add markers
        self.map_widget.set_marker(route_coordinates[0][0], route_coordinates[0][1], text=start_label)
        self.map_widget.set_marker(route_coordinates[-1][0], route_coordinates[-1][1], text=end_label)

    def clear_route(self):
        """Clear the current route from the map"""
        if self.current_route_path:
            self.map_widget.delete(self.current_route_path)
            self.current_route_path = None

    def center_on_location(self, lat, lon, zoom=15):
        """
        Center the map on a specific location.

        Args:
            lat (float): Latitude
            lon (float): Longitude
            zoom (int): Zoom level
        """
        self.map_widget.set_position(lat, lon)
        self.map_widget.set_zoom(zoom)
