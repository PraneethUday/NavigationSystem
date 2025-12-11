"""Application main class"""

from src.backend.data_structures import Trie
from src.backend.services import RoutingService
from src.frontend.ui.main_window import MainWindow


class NavigationApp:
    """
    Main application class that coordinates backend and frontend components.
    """

    def __init__(self, root):
        """
        Initialize the navigation application.

        Args:
            root: Root tkinter widget
        """
        self.root = root
        self.routing_service = RoutingService()
        self.location_trie = Trie()

        # Initialize UI
        self.ui = MainWindow(root, self.on_search)

        # Populate trie with sample cities
        self.populate_locations()

    def populate_locations(self):
        """Populate the location trie with sample cities"""
        cities = [
            "Pappampatti", "Perur", "Punjab", "Pune", "Prague",
            "Utrecht", "Uluru", "Udaipur", "Peelamedu", "Ukkadam",
            "Ettimadai", "Chennai", "Panam", "Paris", "London",
            "New York", "Tokyo", "Sydney", "Dubai", "Singapore"
        ]
        for city in cities:
            self.location_trie.insert(city)

    def on_search(self, start_location, end_location):
        """
        Handle search request from the UI.

        Args:
            start_location (str): Starting location
            end_location (str): Destination location
        """
        try:
            # Calculate route
            route_data = self.routing_service.calculate_route(start_location, end_location)

            # Get directions
            directions = self.routing_service.get_turn_by_turn_directions(route_data['coordinates'])

            # Display on UI
            self.ui.display_route(route_data['coordinates'])
            self.ui.display_directions(
                start_location,
                end_location,
                directions,
                distance=route_data['distance']
            )

        except Exception as e:
            self.ui.display_error(f"Error: {str(e)}")

    def run(self):
        """Start the application"""
        self.ui.run()
