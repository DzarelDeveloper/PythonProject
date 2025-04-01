# Project-15 : Screenshot Tool
# Codesphered01010

import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab, Image, ImageDraw, ImageTk
import os

class ScreenshotTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Tool")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.screenshot_button = tk.Button(self.toolbar, text="Take Screenshot", command=self.take_screenshot)
        self.screenshot_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.toolbar, text="Clear", command=self.clear_canvas, state=tk.DISABLED)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.draw_button = tk.Button(self.toolbar, text="Draw", command=self.activate_draw)
        self.draw_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.image = None
        self.draw_mode = False
        self.last_x, self.last_y = None, None
        self.current_draw = None
        self.drawn_items = []

    def take_screenshot(self):
        self.root.withdraw()
        self.root.after(1000, self.capture_screen)

    def capture_screen(self):
        screenshot = ImageGrab.grab()
        self.image = screenshot
        self.display_image(screenshot)
        self.save_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)
        self.root.deiconify()

    def display_image(self, img):
        self.clear_canvas()
        self.photo_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=tk.NW)

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg"),
                                                                ("All files", "*.*")])
            if file_path:
                self.image.save(file_path)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.drawn_items.clear()

    def activate_draw(self):
        self.draw_mode = not self.draw_mode
        if self.draw_mode:
            self.canvas.bind("<ButtonPress-1>", self.start_drawing)
            self.canvas.bind("<B1-Motion>", self.draw)
            self.draw_button.config(text="Stop Drawing")
        else:
            self.canvas.unbind("<ButtonPress-1>")
            self.canvas.unbind("<B1-Motion>")
            self.draw_button.config(text="Draw")

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        line = self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=2)
        self.drawn_items.append(line)
        if self.image:
            draw = ImageDraw.Draw(self.image)
            draw.line([self.last_x, self.last_y, x, y], fill="black", width=2)
        self.last_x, self.last_y = x, y

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotTool(root)
    root.mainloop()
