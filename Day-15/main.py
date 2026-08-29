# Project-11 : File Manager
# Codesphered01010

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.current_directory = os.getcwd()

        self.path_label = tk.Label(root, text=f"Current Directory: {self.current_directory}", anchor="w")
        self.path_label.pack(fill="both", padx=10, pady=5)

        self.file_listbox = tk.Listbox(root, width=80, height=20)
        self.file_listbox.pack(pady=10)

        self.open_button = tk.Button(root, text="Open", command=self.open_file)
        self.open_button.pack(side="left", padx=5)

        self.rename_button = tk.Button(root, text="Rename", command=self.rename_file)
        self.rename_button.pack(side="left", padx=5)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_file)
        self.delete_button.pack(side="left", padx=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh)
        self.refresh_button.pack(side="left", padx=5)

        self.navigate_button = tk.Button(root, text="Navigate", command=self.navigate)
        self.navigate_button.pack(side="left", padx=5)

        self.refresh()

    def refresh(self):
        """Refresh the file list based on current directory"""
        self.file_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(self.current_directory):
                self.file_listbox.insert(tk.END, item)
        except PermissionError:
            messagebox.showerror("Permission Denied", "You do not have permission to view this folder.")
    
    def open_file(self):
        """Open selected file"""
        selected_file = self.file_listbox.curselection()
        if selected_file:
            file_name = self.file_listbox.get(selected_file[0])
            file_path = os.path.join(self.current_directory, file_name)
            if os.path.isfile(file_path):
                os.startfile(file_path)
            else:
                messagebox.showwarning("Invalid File", "Please select a valid file.")
        else:
            messagebox.showwarning("No Selection", "Please select a file to open.")

    def rename_file(self):
        """Rename selected file"""
        selected_file = self.file_listbox.curselection()
        if selected_file:
            old_name = self.file_listbox.get(selected_file[0])
            old_path = os.path.join(self.current_directory, old_name)
            new_name = filedialog.asksaveasfilename(initialfile=old_name)
            if new_name:
                try:
                    os.rename(old_path, new_name)
                    messagebox.showinfo("Success", "File renamed successfully.")
                    self.refresh()
                except Exception as e:
                    messagebox.showerror("Error", f"Error renaming file: {e}")
        else:
            messagebox.showwarning("No Selection", "Please select a file to rename.")

    def delete_file(self):
        """Delete selected file"""
        selected_file = self.file_listbox.curselection()
        if selected_file:
            file_name = self.file_listbox.get(selected_file[0])
            file_path = os.path.join(self.current_directory, file_name)
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {file_name}?")
            if confirm:
                try:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path) 
                    else:
                        os.remove(file_path) 
                    messagebox.showinfo("Success", f"File {file_name} deleted successfully.")
                    self.refresh()
                except Exception as e:
                    messagebox.showerror("Error", f"Error deleting file: {e}")
        else:
            messagebox.showwarning("No Selection", "Please select a file to delete.")

    def navigate(self):
        """Navigate to a different directory"""
        folder = filedialog.askdirectory(initialdir=self.current_directory)
        if folder:
            self.current_directory = folder
            self.path_label.config(text=f"Current Directory: {self.current_directory}")
            self.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
