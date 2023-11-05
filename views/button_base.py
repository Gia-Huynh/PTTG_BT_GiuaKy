import tkinter as tk

class Button(tk.Button):
    def __init__(self, parent, callback=None):
        super().__init__(parent, text="Upload Image")
        self.callback = callback

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.callback()

    def set_callback(self, callback):
        self.callback = callback