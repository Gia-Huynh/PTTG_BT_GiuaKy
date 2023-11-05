import tkinter as tk
from PIL import Image, ImageTk

class Image_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add a canvas later
        self.label = tk.Label(parent)
        self.label.pack()

    def set_image(self, image):
        # Resize image so it fixes the frame
        size = self.winfo_width(), self.winfo_height()
        print(size)
        image = image.resize(size)
        image = ImageTk.PhotoImage(image)

        self.label.config(image=image)
        self.label.image = image