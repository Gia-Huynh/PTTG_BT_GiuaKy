import tkinter as tk
from PIL import Image, ImageTk

class Image_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.pack_propagate(False)
        self.config(bg='black')

        # self.label = tk.Label(parent)
        self.label = tk.Label(self)
        self.label.pack()

    def set_image(self, image):
        # Resize image so it fixes the frame
        image = ImageTk.PhotoImage(image)

        self.label.config(image=image)
        self.label.image = image