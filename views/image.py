import tkinter as tk

class Image(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add a canvas later
        self.label = tk.Label(self, text="Image")
        self.label.pack()