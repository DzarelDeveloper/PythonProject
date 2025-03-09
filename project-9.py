# Project-9 : Smart Calender
# Codesphered01010

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import datetime
import os
import json

class SmartCalendar:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calendar")
        self.root.geometry("600x500")

        self.events = {}
        self.load_events()

        self.calendar = Calendar(self.root, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=20)

        add_event_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        add_event_button.pack(pady=5)

        show_events_button = tk.Button(self.root, text="Show Events", command=self.show_events)
        show_events_button.pack(pady=5)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        quit_button.pack(pady=20)

    def add_event(self):
        """Add an event for the selected date."""
        selected_date = self.calendar.get_date()

        event_window = tk.Toplevel(self.root)
        event_window.title(f"Add Event on {selected_date}")
        event_window.geometry("400x200")

        tk.Label(event_window, text=f"Add Event for {selected_date}", font=("Arial", 14)).pack(pady=10)
        event_text = tk.Text(event_window, width=40, height=5)
        event_text.pack(pady=10)

        def save_event():
            event_data = event_text.get("1.0", tk.END).strip()
            if not event_data:
                messagebox.showwarning("Empty Event", "Event cannot be empty.")
                return

            if selected_date not in self.events:
                self.events[selected_date] = []

            self.events[selected_date].append(event_data)
            self.save_events()
            messagebox.showinfo("Success", "Event added successfully!")
            event_window.destroy()

        save_button = tk.Button(event_window, text="Save Event", command=save_event)
        save_button.pack(pady=10)

    def show_events(self):
        """Show events for the selected date."""
        selected_date = self.calendar.get_date()
        event_list = self.events.get(selected_date, [])

        event_window = tk.Toplevel(self.root)
        event_window.title(f"Events on {selected_date}")
        event_window.geometry("400x300")

        tk.Label(event_window, text=f"Events for {selected_date}", font=("Arial", 14)).pack(pady=10)

        if event_list:
            for event in event_list:
                tk.Label(event_window, text=f"- {event}", anchor="w").pack(pady=2, padx=20, fill="x")
        else:
            tk.Label(event_window, text="No events found for this date.").pack(pady=10)

    def save_events(self):
        """Save events to a JSON file."""
        with open("events.json", "w") as file:
            json.dump(self.events, file)

    def load_events(self):
        """Load events from a JSON file."""
        if os.path.exists("events.json"):
            with open("events.json", "r") as file:
                self.events = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCalendar(root)
    root.mainloop()
