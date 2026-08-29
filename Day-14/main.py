# Project-14 : Music Player
# Codesphered01010

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

def play_music():
    song = entry_song.get()
    if song != "":
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            label_status.config(text="Musik Sedang Di Putar", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan saat memutar musik: {e}")
    else:
        messagebox.showwarning("Peringatan", "Pilih file musik terlebih dahulu!")

def pause_music():
    pygame.mixer.music.pause()
    label_status.config(text="Musik Dijeda", fg="orange")

def unpause_music():
    pygame.mixer.music.unpause()
    label_status.config(text="Melanjutkan Musik", fg="blue")

def stop_music():
    pygame.mixer.music.stop()
    label_status.config(text="Musik Dihentikan", fg="red")

def choose_song():
    file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac")])
    if file:
        entry_song.delete(0, tk.END)
        entry_song.insert(0, file)

root = tk.Tk()
root.title("Pemutar Musik")
root.geometry("400x400") 
root.config(bg="#282c34") 

header_label = tk.Label(root, text="Pemutar Musik", font=("Helvetica", 16, "bold"), fg="white", bg="#282c34")
header_label.pack(pady=20)

label_song = tk.Label(root, text="Pilih File Musik:", font=("Arial", 12), fg="white", bg="#282c34")
label_song.pack(pady=5)

entry_song = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="sunken")
entry_song.pack(pady=10)

button_choose = tk.Button(root, text="Pilih Musik", command=choose_song, width=20, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
button_choose.pack(pady=5)

button_play = tk.Button(root, text="Play", command=play_music, width=20, font=("Arial", 12), bg="#2196F3", fg="white", relief="raised")
button_play.pack(pady=5)

button_pause = tk.Button(root, text="Pause", command=pause_music, width=20, font=("Arial", 12), bg="#FF9800", fg="white", relief="raised")
button_pause.pack(pady=5)

button_unpause = tk.Button(root, text="Unpause", command=unpause_music, width=20, font=("Arial", 12), bg="#FFC107", fg="white", relief="raised")
button_unpause.pack(pady=5)

button_stop = tk.Button(root, text="Stop", command=stop_music, width=20, font=("Arial", 12), bg="#F44336", fg="white", relief="raised")
button_stop.pack(pady=5)

label_status = tk.Label(root, text="Tidak ada musik yang diputar", font=("Arial", 12, "italic"), fg="gray", bg="#282c34")
label_status.pack(pady=20)

root.mainloop()
