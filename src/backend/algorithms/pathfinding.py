"""Pathfinding algorithms for route calculation"""

try:
    import networkx as nx
except ImportError:
    nx = None


class PathFinder:
    """
    Pathfinding utility class for finding shortest routes using NetworkX.
    Supports various graph types and weighting options.
    """

    @staticmethod
    def find_shortest_path(graph, start_node, end_node, weight='length'):
        """
        Find the shortest path between two nodes using Dijkstra's algorithm.

        Args:
            graph (networkx.Graph): The graph to search
            start_node: The starting node
            end_node: The destination node
            weight (str): The edge weight attribute to use (default: 'length')

        Returns:
            list: List of node IDs representing the path from start to end

        Raises:
            networkx.NetworkXNoPath: If no path exists between the nodes
            ImportError: If NetworkX is not installed
        """
        if nx is None:
            raise ImportError("NetworkX is required for pathfinding. Install with: pip install networkx")
        
        try:
            return nx.shortest_path(graph, start_node, end_node, weight=weight)
        except nx.NetworkXNoPath:
            raise RuntimeError(f"No path found between node {start_node} and {end_node}")
        except Exception as e:
            raise RuntimeError(f"Error finding path: {str(e)}")

    @staticmethod
    def get_path_coordinates(graph, path):
        """
        Convert a path of node IDs to a list of (lat, lon) coordinates.

        Args:
            graph (networkx.Graph): The graph containing node coordinates
            path (list): List of node IDs

        Returns:
            list: List of (latitude, longitude) tuples
        """
        coordinates = []
        for node in path:
            node_data = graph.nodes[node]
            lat = node_data.get('y')
            lon = node_data.get('x')
            if lat is not None and lon is not None:
                coordinates.append((lat, lon))
        return coordinates

    @staticmethod
    def get_path_distance(graph, path):
        """
        Calculate the total distance of a path.

        Args:
            graph (networkx.Graph): The graph with edge lengths
            path (list): List of node IDs

        Returns:
            float: Total distance in the graph's distance unit
        """
        total_distance = 0.0
        for i in range(len(path) - 1):
            edge_data = graph.get_edge_data(path[i], path[i + 1])
            if edge_data:
                # Handle MultiDiGraph where there may be multiple edges
                if isinstance(edge_data, dict):
                    total_distance += edge_data.get('length', 0)
                else:
                    # For MultiDiGraph, edge_data is a dict of dicts
                    for key, data in edge_data.items():
                        total_distance += data.get('length', 0)
                        break  # Use the first edge
        return total_distance
