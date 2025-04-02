# Project-16 :Color-Pick
# Codesphered01010

import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color_code = colorchooser.askcolor(title="Pilih Warna")[1]
    if color_code:
        color_label.config(text=f"Warna: {color_code}", bg=color_code, fg="white" if is_dark_color(color_code) else "black")

def is_dark_color(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    brightness = (r*299 + g*587 + b*114) / 1000 
    return brightness < 128

root = tk.Tk()
root.title("Color Picker")
root.geometry("300x150")

instruction_label = tk.Label(root, text="Klik tombol untuk memilih warna:")
instruction_label.pack(pady=10)

color_button = tk.Button(root, text="Pilih Warna", command=pick_color)
color_button.pack(pady=10)

color_label = tk.Label(root, text="Warna: #FFFFFF", bg="white", width=30, height=2)
color_label.pack(pady=10)

root.mainloop()
