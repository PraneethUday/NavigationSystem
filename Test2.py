import tkinter as tk
from tkinter import ttk, scrolledtext
from tkintermapview import TkinterMapView
import osmnx as ox
import networkx as nx


# Define the N-ary tree node
class NaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find(self, data):
        if self.data == data:
            return self
        for child in self.children:
            found = child.find(data)
            if found:
                return found
        return None


# Define the Trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


# Define the Trie structure
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.collect_all_words(node, prefix)

    def collect_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self.collect_all_words(child_node, prefix + char))
        return words[:5]  # Limit suggestions to 5


# Main Application
class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Navigation Map")
        self.root.geometry("1000x750")
        self.root.configure(bg='#f0f0f0')

        # Initialize N-ary tree and Trie
        self.location_tree = NaryTreeNode("World")
        self.location_trie = Trie()
        self.populate_trie()

        # Active entry field variable to track which entry is active
        self.active_entry = None

        # Setup the GUI
        self.setup_gui()

    def setup_gui(self):
        self.search_frame = tk.Frame(self.root, bg='white', padx=10, pady=10, relief='flat')
        self.search_frame.pack(fill='x', padx=20, pady=5)

        tk.Label(self.search_frame, text="Current Location:", bg='white', font=('Arial', 12)).pack(side='left', padx=5)
        self.current_location_entry = ttk.Entry(self.search_frame, width=30, font=('Arial', 12))
        self.current_location_entry.pack(side='left', padx=5)
        self.current_location_entry.bind("<KeyRelease>", lambda event: self.update_suggestions(event, "current"))
        self.current_location_entry.bind("<FocusIn>", lambda event: self.set_active_entry("current"))

        tk.Label(self.search_frame, text="Destination:", bg='white', font=('Arial', 12)).pack(side='left', padx=5)
        self.destination_entry = ttk.Entry(self.search_frame, width=30, font=('Arial', 12))
        self.destination_entry.pack(side='left', padx=5)
        self.destination_entry.bind("<KeyRelease>", lambda event: self.update_suggestions(event, "destination"))
        self.destination_entry.bind("<FocusIn>", lambda event: self.set_active_entry("destination"))

        self.search_button = tk.Button(self.search_frame, text="Get Directions", command=self.get_directions,
                                       bg='#007BFF', fg='white', font=('Arial', 12, 'bold'), relief='flat')
        self.search_button.pack(side='left', padx=5)

        # Centered suggestion listbox below entries
        self.suggestions_listbox = tk.Listbox(self.root, height=4, width=40, font=('Arial', 12), bg='white')
        self.suggestions_listbox.pack(pady=(5, 10))  # Padding to separate from entries and map
        self.suggestions_listbox.bind("<<ListboxSelect>>", self.select_suggestion)

        # Map widget below suggestion listbox
        self.map_widget = TkinterMapView(self.root, width=800, height=500, corner_radius=10)
        self.map_widget.pack(pady=10)
        self.map_widget.set_position(48.860381, 2.338594)  # Initial position (Paris, France)
        self.map_widget.set_zoom(15)

        self.directions_text = scrolledtext.ScrolledText(self.root, width=60, height=10, wrap=tk.WORD,
                                                         font=('Arial', 12), bg='white', fg='black')
        self.directions_text.pack(pady=10, padx=20)

    def populate_trie(self):
            # Populate the Trie with some city names starting with 'P' and 'U'
            cities = ["Pappampatti", "Perur", "Punjab", "Pune", "Prague", "Utrecht", "Uluru", "Udaipur","Peelamedu","Ukkadam","Ettimadai","Chennai","Panam"]
            for city in cities:
                self.location_trie.insert(city)

    def set_active_entry(self, entry_name):
        self.active_entry = entry_name

    def update_suggestions(self, event, entry_name):
        typed_text = self.current_location_entry.get() if entry_name == "current" else self.destination_entry.get()
        suggestions = self.location_trie.search_prefix(typed_text)

        # Clear current suggestions in the listbox
        self.suggestions_listbox.delete(0, tk.END)

        # Insert new suggestions
        for suggestion in suggestions:
            self.suggestions_listbox.insert(tk.END, suggestion)

    def select_suggestion(self, event):
        # Get selected suggestion and update the active entry field
        selection = self.suggestions_listbox.curselection()
        if selection:
            selected_city = self.suggestions_listbox.get(selection[0])
            if self.active_entry == "current":
                self.current_location_entry.delete(0, tk.END)
                self.current_location_entry.insert(0, selected_city)
            elif self.active_entry == "destination":
                self.destination_entry.delete(0, tk.END)
                self.destination_entry.insert(0, selected_city)

            # Clear suggestions once a selection is made
            self.suggestions_listbox.delete(0, tk.END)

    def get_directions(self):
        current_location = self.current_location_entry.get()
        destination = self.destination_entry.get()

        # Clear previous directions
        self.directions_text.delete(1.0, tk.END)
        self.directions_text.insert(tk.END, f"Current Location: {current_location}\n")
        self.directions_text.insert(tk.END, f"Destination: {destination}\n")

        try:
            start_point = ox.geocode(current_location)
            end_point = ox.geocode(destination)

            G = ox.graph_from_point(start_point, dist=5000, network_type='drive')
            start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
            end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])

            # Get the shortest path using Dijkstra's algorithm based on edge length
            route = nx.shortest_path(G, start_node, end_node, weight='length')
            route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

            self.map_widget.set_position(start_point[0], start_point[1])
            self.map_widget.set_zoom(12)
            self.map_widget.set_path(route_coords, color="blue", width=2)
            self.map_widget.set_marker(route_coords[0][0], route_coords[0][1], text="Start")
            self.map_widget.set_marker(route_coords[-1][0], route_coords[-1][1], text="End")
            self.display_directions(route_coords)

        except Exception as e:
            self.directions_text.insert(tk.END, f"Error: {str(e)}\n")

    def display_directions(self, route_coords):
        for i in range(len(route_coords) - 1):
            self.directions_text.insert(tk.END,
                                        f"From ({route_coords[i][0]}, {route_coords[i][1]}) to ({route_coords[i + 1][0]}, {route_coords[i + 1][1]})\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()
