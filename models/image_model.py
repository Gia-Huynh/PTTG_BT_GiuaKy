from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import math

class Image_Model():
    def __init__(self):
        self.image_path = None
        self.image_data = None
        self.image_cv = None

    def get_image_path(self):
        return self.image_path
    
    def get_image_data(self):
        return self.image_data
    
    def get_image_cv(self):
        return self.image_cv
    
    def set_image_path(self, image_path):
        # Valid path
        if image_path:
            # Check if path is available and a valid image
            try:
                image_tk = Image.open(image_path)
                image_cv = cv2.imread(image_path, 0)
            except:
                return False
            self.image_path = image_path

            # Set image data
            self.image_data = image_tk
            # Find the nearest squared number for the image size
            image_size = math.sqrt(min(image_cv.shape[:2]))
            image_size = int(image_size)
            image_size = image_size ** 2
            # Resize the image
            self.image_cv = cv2.resize(image_cv, (image_size, image_size))
        return True
    
    def reset(self):
        self.image_path = None
        self.image_data = None