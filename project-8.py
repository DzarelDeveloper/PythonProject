# Project-8 : Enc & Dec Text
# Codesphered01010

import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

class EnkripsiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enkripsi & Dekripsi Pesan")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        main_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        ttk.Label(main_frame, text="Enkripsi & Dekripsi Pesan", font=("Helvetica", 16, "bold"), background="#ffffff").pack(pady=10)

        ttk.Label(main_frame, text="Masukkan Pesan:", background="#ffffff", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(5, 0))
        self.input_text = tk.Text(main_frame, height=3, width=50, font=("Arial", 9), wrap="word", relief="ridge", bd=1)
        self.input_text.pack(padx=20, pady=5)

        ttk.Label(main_frame, text="Shift (Pergeseran Huruf):", background="#ffffff", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(5, 0))
        self.shift_entry = ttk.Entry(main_frame, width=5, font=("Arial", 10))
        self.shift_entry.pack(anchor="w", padx=20, pady=5)

        button_frame = tk.Frame(main_frame, bg="#ffffff")
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Enkripsi", width=15, command=self.enkripsi_pesan).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(button_frame, text="Dekripsi", width=15, command=self.dekripsi_pesan).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(main_frame, text="Hasil:", background="#ffffff", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(5, 0))
        self.output_text = tk.Text(main_frame, height=3, width=50, font=("Arial", 9), state='disabled', wrap="word", bg="#f9f9f9", relief="ridge", bd=1)
        self.output_text.pack(padx=20, pady=5)

        ttk.Button(main_frame, text="Copy Hasil", width=15, command=self.copy_hasil).pack(pady=5)

    def enkripsi_pesan(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            if not text:
                messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong!")
                return
            result = caesar_cipher(text, shift, mode="encrypt")
            self.tampilkan_output(result)
        except ValueError:
            messagebox.showerror("Error", "Shift harus berupa angka!")

    def dekripsi_pesan(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            if not text:
                messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong!")
                return
            result = caesar_cipher(text, shift, mode="decrypt")
            self.tampilkan_output(result)
        except ValueError:
            messagebox.showerror("Error", "Shift harus berupa angka!")

    def tampilkan_output(self, result):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')

    def copy_hasil(self):
        result = self.output_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.root.update()
            messagebox.showinfo("Berhasil", "Hasil telah disalin ke clipboard.")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada hasil untuk disalin!")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnkripsiApp(root)
    root.mainloop()
