import tkinter as tk

from views.button_base import Button

class Control_View(tk.Frame):
    def __init__(self, parent, image_upload_callback=None):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="Control")
        self.label.pack()

        self.buttons = []

        # Button for upload image
        self.upload_button = Button(self, image_upload_callback)
        self.upload_button.pack(side=tk.TOP, fill=tk.X)

        # Slider for resize image
        self.slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.slider.set(50)
        self.slider.pack(side=tk.TOP, fill=tk.X)

    def set_image_callback(self, callback):
        self.upload_button.set_callback(callback)