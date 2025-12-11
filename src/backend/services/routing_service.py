"""Routing service for handling navigation requests"""

try:
    import osmnx as ox
except ImportError:
    ox = None

from src.backend.algorithms.pathfinding import PathFinder


class RoutingService:
    """
    Service for handling all routing-related operations.
    Manages geocoding, graph creation, pathfinding, and direction generation.
    """

    def __init__(self, graph_distance=5000, network_type='drive'):
        """
        Initialize the routing service.

        Args:
            graph_distance (int): Distance in meters for the road network around a point
            network_type (str): Type of network ('drive', 'walk', 'bike', etc.)
        """
        self.graph_distance = graph_distance
        self.network_type = network_type
        self.current_graph = None

    def get_coordinates(self, location_name):
        """
        Get latitude and longitude coordinates for a location name.

        Args:
            location_name (str): The name of the location

        Returns:
            tuple: (latitude, longitude)

        Raises:
            ValueError: If the location cannot be geocoded
        """
        if ox is None:
            raise ImportError("OSMnx is required for geocoding. Install with: pip install osmnx")
        
        try:
            return ox.geocode(location_name)
        except Exception as e:
            raise ValueError(f"Could not find location '{location_name}': {str(e)}")

    def get_road_network(self, coordinates):
        """
        Get the road network graph for a given location.

        Args:
            coordinates (tuple): (latitude, longitude)

        Returns:
            networkx.MultiDiGraph: The road network graph

        Raises:
            RuntimeError: If the graph cannot be created
        """
        if ox is None:
            raise ImportError("OSMnx is required for road network. Install with: pip install osmnx")
        
        try:
            return ox.graph_from_point(coordinates, dist=self.graph_distance, network_type=self.network_type)
        except Exception as e:
            raise RuntimeError(f"Could not create road network: {str(e)}")

    def get_nearest_node(self, graph, coordinates):
        """
        Find the nearest node in the graph to the given coordinates.

        Args:
            graph (networkx.MultiDiGraph): The road network graph
            coordinates (tuple): (latitude, longitude)

        Returns:
            The node ID of the nearest node
        """
        if ox is None:
            raise ImportError("OSMnx is required for nearest node. Install with: pip install osmnx")
        
        return ox.distance.nearest_nodes(graph, coordinates[1], coordinates[0])

    def calculate_route(self, start_location, end_location):
        """
        Calculate the optimal route between two locations.

        Args:
            start_location (str): Starting location name
            end_location (str): Destination location name

        Returns:
            dict: Dictionary containing:
                - 'path': list of node IDs
                - 'coordinates': list of (lat, lon) tuples
                - 'distance': total distance in meters
                - 'start_coords': (lat, lon) of start
                - 'end_coords': (lat, lon) of end

        Raises:
            ValueError: If locations cannot be geocoded
            RuntimeError: If route cannot be calculated
        """
        # Get coordinates
        start_coords = self.get_coordinates(start_location)
        end_coords = self.get_coordinates(end_location)

        # Get road network
        graph = self.get_road_network(start_coords)
        self.current_graph = graph

        # Find nearest nodes
        start_node = self.get_nearest_node(graph, start_coords)
        end_node = self.get_nearest_node(graph, end_coords)

        # Find path
        path = PathFinder.find_shortest_path(graph, start_node, end_node, weight='length')

        # Get coordinates
        coordinates = PathFinder.get_path_coordinates(graph, path)

        # Calculate distance
        distance = PathFinder.get_path_distance(graph, path)

        return {
            'path': path,
            'coordinates': coordinates,
            'distance': distance,
            'start_coords': start_coords,
            'end_coords': end_coords,
        }

    def get_turn_by_turn_directions(self, coordinates):
        """
        Generate turn-by-turn directions from a list of coordinates.

        Args:
            coordinates (list): List of (lat, lon) tuples

        Returns:
            list: List of direction strings
        """
        directions = []
        for i in range(len(coordinates) - 1):
            direction = (f"From ({coordinates[i][0]:.6f}, {coordinates[i][1]:.6f}) "
                        f"to ({coordinates[i + 1][0]:.6f}, {coordinates[i + 1][1]:.6f})")
            directions.append(direction)
        return directions
