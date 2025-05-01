import tkinter as tk
from tkinter import ttk, scrolledtext
from tkintermapview import TkinterMapView
import osmnx as ox

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Navigation Map")

        # Create a frame for the search bar
        self.search_frame = tk.Frame(self.root, bg='lightgray', padx=10, pady=10)
        self.search_frame.pack(fill='x')

        # Create a label and entry for current location
        tk.Label(self.search_frame, text="Current Location:", bg='lightgray').pack(side='left', padx=5)
        self.current_location_entry = ttk.Entry(self.search_frame, width=30)
        self.current_location_entry.pack(side='left', padx=5)

        # Create a label and entry for destination
        tk.Label(self.search_frame, text="Destination:", bg='lightgray').pack(side='left', padx=5)
        self.destination_entry = ttk.Entry(self.search_frame, width=30)
        self.destination_entry.pack(side='left', padx=5)

        # Create a "Get Directions" button
        self.search_button = tk.Button(self.search_frame, text="Get Directions", command=self.get_directions, bg='blue', fg='white', relief='raised')
        self.search_button.pack(side='left', padx=5)

        # Add hover effects for the search button
        self.search_button.bind("<Enter>", self.on_hover)
        self.search_button.bind("<Leave>", self.on_leave)

        # Create a map widget
        self.map_widget = TkinterMapView(self.root, width=800, height=600, corner_radius=0)
        self.map_widget.pack()

        # Create a scrolled text area for directions
        self.directions_text = scrolledtext.ScrolledText(self.root, width=60, height=10, wrap=tk.WORD)
        self.directions_text.pack(pady=10)

        # Set the initial map position and zoom
        self.map_widget.set_position(48.860381, 2.338594)  # Paris, France
        self.map_widget.set_zoom(15)

        self.route_path = None  # Track the route path for deletion

    def get_directions(self):
        # Get the current location and destination
        current_location = self.current_location_entry.get()
        destination = self.destination_entry.get()

        self.directions_text.delete(1.0, tk.END)  # Clear previous directions
        self.directions_text.insert(tk.END, f"Current Location: {current_location}\n")
        self.directions_text.insert(tk.END, f"Destination: {destination}\n")

        try:
            # Get coordinates for the current location and destination
            start_point = ox.geocode(current_location)
            end_point = ox.geocode(destination)

            # Get the graph for the area (increased radius to 5000 meters)
            G = ox.graph_from_point(start_point, dist=5000, network_type='drive')

            # Get the nearest nodes to the start and end points
            start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
            end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])

            # Get the route
            route = ox.shortest_path(G, start_node, end_node)

            # Plot the route on the map
            route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]
            self.map_widget.set_position(start_point[0], start_point[1])
            self.map_widget.set_zoom(12)

            # Remove any previous route
            if self.route_path:
                self.map_widget.delete(self.route_path)

            # Draw the route on the map
            self.route_path = self.map_widget.set_path(route_coords, color="blue", width=2)

            # Mark the start and end points
            self.map_widget.set_marker(route_coords[0][0], route_coords[0][1], text="Start")
            self.map_widget.set_marker(route_coords[-1][0], route_coords[-1][1], text="End")

            # Display directions in the text area
            self.display_directions(route_coords)

        except Exception as e:
            self.directions_text.insert(tk.END, f"Error: {str(e)}\n")

    def display_directions(self, route_coords):
        # Display the route coordinates in the text area
        for i in range(len(route_coords) - 1):
            self.directions_text.insert(tk.END, f"From ({route_coords[i][0]}, {route_coords[i][1]}) to ({route_coords[i+1][0]}, {route_coords[i+1][1]})\n")

    def on_hover(self, event):
        self.search_button.config(relief='flat')

    def on_leave(self, event):
        self.search_button.config(relief='raised')

if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()
