# Project-6 : DIARY
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

def countdown_timer():
    try:
        total_seconds = int(hours_var.get()) * 3600 + int(minutes_var.get()) * 60 + int(seconds_var.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the timer!")
        return

    if total_seconds <= 0:
        messagebox.showerror("Error", "Please set a time greater than 0!")
        return

    start_button.config(state="disabled")
    reset_button.config(state="normal")
    while total_seconds > 0 and running_timer:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
        time.sleep(1)
        total_seconds -= 1

    if total_seconds == 0 and running_timer:
        timer_label.config(text="00:00:00")
        messagebox.showinfo("Time's up!", "The timer has finished!")
        stop_timer()

def start_timer():
    global running_timer
    running_timer = True
    timer_thread = Thread(target=countdown_timer, daemon=True)
    timer_thread.start()

def stop_timer():
    global running_timer
    running_timer = False
    start_button.config(state="normal")
    reset_button.config(state="disabled")

def reset_timer():
    stop_timer()
    timer_label.config(text="00:00:00")
    hours_var.set("0")
    minutes_var.set("0")
    seconds_var.set("0")

root = tk.Tk()
root.title("Multi-Function Timer")
root.geometry("300x300")

running_timer = False

timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36), fg="blue")
timer_label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

hours_var = tk.StringVar(value="0")
minutes_var = tk.StringVar(value="0")
seconds_var = tk.StringVar(value="0")

tk.Label(frame, text="Hours:").grid(row=0, column=0)
tk.Entry(frame, textvariable=hours_var, width=5).grid(row=0, column=1)

tk.Label(frame, text="Minutes:").grid(row=0, column=2)
tk.Entry(frame, textvariable=minutes_var, width=5).grid(row=0, column=3)

tk.Label(frame, text="Seconds:").grid(row=0, column=4)
tk.Entry(frame, textvariable=seconds_var, width=5).grid(row=0, column=5)

start_button = tk.Button(root, text="Start", command=start_timer, bg="green", fg="white", width=10)
start_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_timer, bg="red", fg="white", width=10, state="disabled")
reset_button.pack(pady=5)

root.mainloop()
