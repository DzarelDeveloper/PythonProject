# Project-13 : Register & Login Form
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

def login():
    username = entry_username.get()
    password = entry_password.get()

    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                user_data = user.strip().split(",")
                if username == user_data[0] and password == user_data[1]:
                    messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
                    return
    messagebox.showerror("Login Gagal", "Username atau password salah.")

def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
        return

    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                user_data = user.strip().split(",")
                if username == user_data[0]:
                    messagebox.showerror("Error", "Username sudah terdaftar!")
                    return

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
        messagebox.showinfo("Registrasi Berhasil", "Akun berhasil didaftarkan!")

def toggle_password_visibility():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
        button_show_password.config(text="Sembunyikan Password")
    else:
        entry_password.config(show="*")
        button_show_password.config(text="Tampilkan Password")

root = tk.Tk()
root.title("Sistem Login Sederhana")
root.geometry("450x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))
style.configure("MainFrame.TFrame", background="#f7f7f7")

frame = ttk.Frame(root, padding="20", style="MainFrame.TFrame")
frame.pack(fill="both", expand=True)

label_title = ttk.Label(frame, text="Sistem Login", font=("Helvetica", 16, "bold"), anchor="center")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_username = ttk.Label(frame, text="Username:")
label_username.grid(row=1, column=0, sticky="e", padx=10, pady=10)
entry_username = ttk.Entry(frame, width=30)
entry_username.grid(row=1, column=1, padx=10, pady=10)

label_password = ttk.Label(frame, text="Password:")
label_password.grid(row=2, column=0, sticky="e", padx=10, pady=10)
entry_password = ttk.Entry(frame, show="*", width=30)
entry_password.grid(row=2, column=1, padx=10, pady=10)

button_show_password = ttk.Button(frame, text="Tampilkan Password", command=toggle_password_visibility)
button_show_password.grid(row=3, column=1, sticky="w", padx=10, pady=5)

button_login = ttk.Button(frame, text="Login", command=login, width=15)
button_login.grid(row=4, column=0, padx=10, pady=20, sticky="e")

button_register = ttk.Button(frame, text="Register", command=register, width=15)
button_register.grid(row=4, column=1, padx=10, pady=20, sticky="w")

label_footer = ttk.Label(frame, text="© 2024 Sistem Login Sederhana", font=("Helvetica", 8), anchor="center")
label_footer.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
