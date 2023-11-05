# Image class for the image object of tkinter

from tkinter import *
from PIL import Image, ImageTk

class Image_Model():
    def __init__(self):
        self.image_path = None
        self.image_data = None

    def get_image_path(self):
        return self.image_path
    
    def get_image_data(self):
        return self.image_data
    
    def set_image_path(self, image_path):
        # Valid path
        if image_path:
            # Check if path is available and a valid image
            try:
                image = Image.open(image_path)
            except:
                return False
            self.image_path = image_path

            # Convert image to Tkinter readable format
            # image = ImageTk.PhotoImage(image)

            # Set image data
            self.image_data = image
        return True