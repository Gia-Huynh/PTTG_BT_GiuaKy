import tkinter as tk
from PIL import Image, ImageTk

class PCA_Controller:
    def __init__(self, image_model, image_view):
        self.image_model = image_model
        self.image_view = image_view

        # Init things here

        # Binding thingy
        self.image_view.control.back_button.bind("<Button-1>", self.back)

    def back(self, event):
        self.image_view.set_default()
        self.image_view.display.set_image(self.image_model.get_image_data())
        return True
