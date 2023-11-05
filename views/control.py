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

        # Generate a bunch of buttons for placeholder
        for i in range(2):
            button = tk.Button(self, text=f"Button {i}")
            self.buttons.append(button)
            self.buttons[i].pack(side=tk.TOP, fill=tk.X)

    def set_image_callback(self, callback):
        self.upload_button.set_callback(callback)