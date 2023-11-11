import tkinter as tk

from views.button_base import Button

class Control_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="Control")
        self.label.pack()

        # Button for image
        self.upload_button = tk.Button(self, text="Upload Image")
        self.upload_button.pack(side=tk.TOP, fill=tk.X)

        self.reset_button = tk.Button(self, text="Reset image")
        self.reset_button.pack(side=tk.BOTTOM, fill=tk.X)

        # For svd demostration
        self.svd_toggle = False
        self.svd_button = Button(self)
        self.svd_button.config(text="SVD: OFF")
        self.svd_button.pack_forget()

    def toggle_svd(self, value):
        self.svd_toggle = value
        if self.svd_toggle: # If the toggle is on, show the button
            self.svd_button.pack(side=tk.TOP, fill=tk.X)
            self.svd_button.config(text="SVD: ON")

        else: # If the toggle is off, hide the button
            self.svd_button.pack_forget()
            self.svd_button.config(text="SVD: OFF")