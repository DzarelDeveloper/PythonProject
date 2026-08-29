# Project-18 : Transcipto
# Codesphered01010

import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

class VoiceTranscriptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transcripto")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Tekan tombol untuk mulai merekam suara", font=("Arial", 14))
        self.label.pack(pady=20)

        self.transcription_area = tk.Text(root, wrap=tk.WORD, height=10, width=40)
        self.transcription_area.pack(pady=10)

        self.record_button = tk.Button(root, text="Rekam Suara", command=self.record_audio, bg="lightblue", font=("Arial", 12))
        self.record_button.pack(pady=20)

    def record_audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.config(text="Mendengarkan...") 
            audio = recognizer.listen(source)

            self.label.config(text="Mendengarkan selesai. Mencoba mentranskripsi...")  
            try:
                transcription = recognizer.recognize_google(audio, language="id-ID")  
                self.transcription_area.delete(1.0, tk.END)  
                self.transcription_area.insert(tk.END, transcription)  
                self.label.config(text="Transkripsi selesai.")  
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Tidak dapat mengenali suara.")
                self.label.config(text="Kesalahan: Tidak dapat mengenali suara.")  
            except sr.RequestError:
                messagebox.showerror("Error", "Tidak dapat terhubung ke layanan pengenalan suara.")
                self.label.config(text="Kesalahan: Tidak dapat terhubung ke layanan.") 

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceTranscriptionApp(root)
    root.mainloop()