"""Directions panel component for displaying route information"""

import tkinter as tk
from tkinter import scrolledtext


class DirectionsPanel:
    """
    Panel for displaying detailed directions and route information.
    """

    def __init__(self, parent):
        """
        Initialize the directions panel.

        Args:
            parent: Parent tkinter widget
        """
        self.parent = parent
        self.text_widget = None

    def create(self):
        """Create and layout the directions panel"""
        self.text_widget = scrolledtext.ScrolledText(
            self.parent,
            width=60,
            height=10,
            wrap=tk.WORD,
            font=('Arial', 12),
            bg='white',
            fg='black'
        )
        self.text_widget.pack(pady=10, padx=20)

    def display_directions(self, start_location, end_location, directions, distance=None):
        """
        Display directions in the text widget.

        Args:
            start_location (str): Starting location name
            end_location (str): Destination location name
            directions (list): List of direction strings
            distance (float): Total distance in meters (optional)
        """
        self.clear()

        # Header
        self.text_widget.insert(tk.END, f"Route from {start_location} to {end_location}\n")
        self.text_widget.insert(tk.END, "=" * 60 + "\n\n")

        # Distance
        if distance is not None:
            distance_km = distance / 1000
            self.text_widget.insert(tk.END, f"Total Distance: {distance_km:.2f} km\n\n")

        # Directions
        self.text_widget.insert(tk.END, "Turn-by-Turn Directions:\n")
        self.text_widget.insert(tk.END, "-" * 60 + "\n")
        for i, direction in enumerate(directions, 1):
            self.text_widget.insert(tk.END, f"{i}. {direction}\n")

        self.text_widget.config(state=tk.DISABLED)

    def display_error(self, error_message):
        """
        Display an error message.

        Args:
            error_message (str): The error message to display
        """
        self.clear()
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, "Error\n")
        self.text_widget.insert(tk.END, "=" * 60 + "\n\n")
        self.text_widget.insert(tk.END, error_message + "\n")
        self.text_widget.config(state=tk.DISABLED)

    def clear(self):
        """Clear all text from the directions panel"""
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
