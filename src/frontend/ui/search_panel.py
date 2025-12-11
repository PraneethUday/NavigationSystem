"""Search panel component for location input"""

import tkinter as tk
from tkinter import ttk


class SearchPanel:
    """
    Panel for searching and selecting start and destination locations.
    Includes location entry fields and search button.
    """

    def __init__(self, parent, on_search_callback):
        """
        Initialize the search panel.

        Args:
            parent: Parent tkinter widget
            on_search_callback: Callback function when search is performed
        """
        self.parent = parent
        self.on_search_callback = on_search_callback
        self.frame = None
        self.current_location_entry = None
        self.destination_entry = None
        self.suggestions_listbox = None
        self.active_entry = None

    def create(self):
        """Create and layout the search panel"""
        self.frame = tk.Frame(self.parent, bg='white', padx=10, pady=10, relief='flat')
        self.frame.pack(fill='x', padx=20, pady=5)

        # Current location
        tk.Label(self.frame, text="Current Location:", bg='white', font=('Arial', 12)).pack(side='left', padx=5)
        self.current_location_entry = ttk.Entry(self.frame, width=30, font=('Arial', 12))
        self.current_location_entry.pack(side='left', padx=5)
        self.current_location_entry.bind("<FocusIn>", lambda event: self.set_active_entry("current"))

        # Destination
        tk.Label(self.frame, text="Destination:", bg='white', font=('Arial', 12)).pack(side='left', padx=5)
        self.destination_entry = ttk.Entry(self.frame, width=30, font=('Arial', 12))
        self.destination_entry.pack(side='left', padx=5)
        self.destination_entry.bind("<FocusIn>", lambda event: self.set_active_entry("destination"))

        # Search button
        search_button = tk.Button(
            self.frame,
            text="Get Directions",
            command=self.on_search_clicked,
            bg='#007BFF',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat'
        )
        search_button.pack(side='left', padx=5)

        # Suggestions listbox
        self.suggestions_listbox = tk.Listbox(self.parent, height=4, width=40, font=('Arial', 12), bg='white')
        self.suggestions_listbox.pack(pady=(5, 10))
        self.suggestions_listbox.bind("<<ListboxSelect>>", self.on_suggestion_selected)

    def set_active_entry(self, entry_name):
        """Set which entry field is currently active"""
        self.active_entry = entry_name

    def on_search_clicked(self):
        """Handle search button click"""
        start_location = self.current_location_entry.get().strip()
        end_location = self.destination_entry.get().strip()

        if start_location and end_location:
            self.on_search_callback(start_location, end_location)

    def on_suggestion_selected(self, event):
        """Handle suggestion selection from listbox"""
        selection = self.suggestions_listbox.curselection()
        if selection:
            selected_city = self.suggestions_listbox.get(selection[0])
            if self.active_entry == "current":
                self.current_location_entry.delete(0, tk.END)
                self.current_location_entry.insert(0, selected_city)
            elif self.active_entry == "destination":
                self.destination_entry.delete(0, tk.END)
                self.destination_entry.insert(0, selected_city)

            self.suggestions_listbox.delete(0, tk.END)

    def update_suggestions(self, suggestions):
        """Update the suggestions listbox"""
        self.suggestions_listbox.delete(0, tk.END)
        for suggestion in suggestions:
            self.suggestions_listbox.insert(tk.END, suggestion)

    def get_locations(self):
        """Get the current location values"""
        return {
            'start': self.current_location_entry.get().strip(),
            'destination': self.destination_entry.get().strip(),
        }

    def clear(self):
        """Clear all input fields"""
        self.current_location_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.suggestions_listbox.delete(0, tk.END)
