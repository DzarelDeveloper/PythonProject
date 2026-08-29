# Project-12 : StudyTime
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import time

class StudyTimerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Aplikasi Pengelola Waktu Belajar")
        self.window.geometry("400x300")
        self.window.configure(bg="#f2f2f2")
        
        self.study_time = 0
        self.break_time = 0
        
        self.timer_running = False
        self.current_time = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.window, text="Pengelola Waktu Belajar", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

        tk.Label(self.window, text="Waktu Belajar (menit):", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
        self.study_entry = tk.Entry(self.window, font=("Arial", 12), width=10)
        self.study_entry.pack(pady=5)

        tk.Label(self.window, text="Waktu Istirahat (menit):", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
        self.break_entry = tk.Entry(self.window, font=("Arial", 12), width=10)
        self.break_entry.pack(pady=5)

        self.start_button = tk.Button(self.window, text="Mulai Belajar", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.start_timer)
        self.start_button.pack(pady=20)

        self.timer_label = tk.Label(self.window, text="00:00", font=("Arial", 24), bg="#f2f2f2", fg="#333333")
        self.timer_label.pack(pady=10)

        self.history_button = tk.Button(self.window, text="Lihat Riwayat", font=("Arial", 12), bg="#2196F3", fg="white", command=self.show_history)
        self.history_button.pack(pady=10)

    def start_timer(self):
        try:
            self.study_time = int(self.study_entry.get())
            self.break_time = int(self.break_entry.get())
        except ValueError:
            messagebox.showwarning("Input Error", "Masukkan angka valid untuk waktu belajar dan istirahat.")
            return

        if self.study_time <= 0 or self.break_time <= 0:
            messagebox.showwarning("Input Error", "Waktu belajar dan istirahat harus lebih dari 0 menit.")
            return
        
        self.timer_running = True
        self.current_time = self.study_time * 60
        self.update_timer()
        self.start_button.config(state="disabled") 

    def update_timer(self):
        if self.timer_running:
            minutes, seconds = divmod(self.current_time, 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.timer_label.config(text=time_str)

            if self.current_time > 0:
                self.current_time -= 1
                self.window.after(1000, self.update_timer)
            else:
                self.handle_time_up()

    def handle_time_up(self):
        if self.current_time == 0:
            if self.study_time > 0:
                self.study_time = 0
                self.current_time = self.break_time * 60
                messagebox.showinfo("Waktu Belajar Selesai", "Waktu belajar selesai! Saatnya istirahat.")
                self.start_button.config(state="normal") 
                self.timer_running = False
                self.update_timer()
            else:
                messagebox.showinfo("Istirahat Selesai", "Waktu istirahat selesai! Kembali belajar.")
                self.study_time = 0
                self.start_button.config(state="normal") 
                self.timer_running = False
                self.update_timer()

    def show_history(self):
        messagebox.showinfo("Riwayat Belajar", "Fitur riwayat belum tersedia pada versi ini.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = StudyTimerApp()
    app.run()
