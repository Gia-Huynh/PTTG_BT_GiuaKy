import numpy as np
import cv2
import matplotlib.pyplot as plt 
from PIL import Image, ImageTk

from utils.svd import svd

class SVD_Controller:
    def __init__(self, image_model, image_view):
        self.image_model = image_model
        self.image_view = image_view

        self.image = image_model.get_image_cv()

        U, S, V = svd(self.image)
        self.U = U
        self.S = S
        self.V = V

        # Get the k number
        max_k = min(self.image.shape)
        self.image_view.control.update_max_k(max_k)

        # Update the image size file

        # Update the distance

        # Update the image
        self.image_view.display.set_image(self.cv2_to_pil(self.get_image_approximation(max_k)))

        # Binding thingy
        self.image_view.control.compression_submit_button.bind("<Button-1>", self.submit_compression)
        self.image_view.control.back_button.bind("<Button-1>", self.back)

    def back(self, event):
        self.image_view.set_default()
        self.image_view.display.set_image(self.image_model.get_image_data())
        return True

    def cv2_to_pil(self, data):
        return Image.fromarray(data)

    def get_image_approximation(self, r):
        img_approx = self.U[:, :r] @ self.S[0:r, :r] @ self.V[:r, :]
        return img_approx
    
    def get_loss(self, r):
        img_approx = self.get_image_approximation(r)
        loss = np.sum(np.square(self.image - img_approx))
        return loss
    
    def submit_compression(self, event):
        # Get the k number from the slider
        r = self.image_view.control.compression_rate_slider.get()

        # Get the image approximation
        img_approx = self.get_image_approximation(r)

        # Update the image size file

        # Update the distance file
        loss = self.get_loss(r)
        self.image_view.control.distance_values.config(text=str(loss))

        # Update the image
        # Add the compress image next to the original image
        new_image = np.hstack((self.image, img_approx))

        # Convert the image to PIL format
        new_image = self.cv2_to_pil(new_image)
        self.image_view.display.set_image(new_image)