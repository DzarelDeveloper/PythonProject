# Project-7 : Password Manager
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import json
import random
import string

PASSWORD_FILE = "passwords.json"

def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def add_password():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if not website or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    passwords = load_passwords()
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)
    messagebox.showinfo("Success", f"Password for {website} saved successfully!")
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def search_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showwarning("Warning", "Please enter a website name!")
        return
    
    passwords = load_passwords()
    if website in passwords:
        details = passwords[website]
        messagebox.showinfo("Password Found", f"Website: {website}\nUsername: {details['username']}\nPassword: {details['password']}")
    else:
        messagebox.showerror("Error", f"No details found for {website}!")

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x400")

tk.Label(root, text="Website:").pack(pady=5, anchor="w")
website_entry = tk.Entry(root, width=50)
website_entry.pack()

tk.Label(root, text="Username:").pack(pady=5, anchor="w")
username_entry = tk.Entry(root, width=50)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=5, anchor="w")
password_entry = tk.Entry(root, width=50)
password_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_button.pack(pady=10)

add_button = tk.Button(root, text="Add Password", command=add_password, bg="green", fg="white")
add_button.pack(pady=10)

search_button = tk.Button(root, text="Search Password", command=search_password, bg="orange", fg="white")
search_button.pack(pady=10)

root.mainloop()

 