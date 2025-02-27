# Project-5 : DIARY
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import time

def save_diary():
    content = diary_text.get("1.0", tk.END).strip()
    if content:
        with open("daily_diary.txt", "a") as f:
            f.write(content + "\n")
            f.write("---- Entry Saved on " + time.strftime("%Y-%m-%d %H:%M:%S") + " ----\n\n")
        messagebox.showinfo("Success", "Diary saved successfully!")
        diary_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Diary is empty!")

root = tk.Tk()
root.title("Daily Diary")
root.geometry("400x300")

tk.Label(root, text="Write your daily notes below:").pack(pady=5)
diary_text = tk.Text(root, height=12, width=40)
diary_text.pack(pady=10)

save_button = tk.Button(root, text="Save", command=save_diary)
save_button.pack(pady=5)

root.mainloop()
