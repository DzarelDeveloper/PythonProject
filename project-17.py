# Project-17 : PicWm
# Codesphered01010

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

def open_image():
    global img, img_display
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img_display = ImageTk.PhotoImage(img.resize((400, 300)))  
        canvas.create_image(200, 150, image=img_display)

def add_watermark():
    global img, img_display
    if img:
        try:
            watermark_text = entry_text.get()
            if not watermark_text:
                messagebox.showwarning("Warning", "Please enter watermark text!")
                return
            
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("arial.ttf", 30)  
            width, height = img.size
            
            text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            position = (width - text_width - 10, height - text_height - 10)
            draw.text(position, watermark_text, (255, 255, 255), font=font)  
            
            img_display = ImageTk.PhotoImage(img.resize((400, 300)))
            canvas.create_image(200, 150, image=img_display)
            
            messagebox.showinfo("Success", "Watermark added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add watermark: {e}")
    else:
        messagebox.showwarning("Warning", "Please open an image first!")

def save_image():
    if img:
        try:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                img.save(save_path)
                messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")
    else:
        messagebox.showwarning("Warning", "No image to save!")

root = tk.Tk()
root.title("Watermark App")

canvas = tk.Canvas(root, width=400, height=300, bg="gray")
canvas.pack()

frame = tk.Frame(root)
frame.pack(pady=10)
tk.Label(frame, text="Watermark Text:").pack(side=tk.LEFT)
entry_text = tk.Entry(frame, width=20)
entry_text.pack(side=tk.LEFT)

btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=5)

btn_add_watermark = tk.Button(root, text="Add Watermark", command=add_watermark)
btn_add_watermark.pack(pady=5)

btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack(pady=5)

root.mainloop()
 