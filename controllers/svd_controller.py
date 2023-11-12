import numpy as np
import cv2
import matplotlib.pyplot as plt 
from PIL import Image, ImageTk

from utils.svd import svd
import constant.path as path

class SVD_Controller:
    def __init__(self, image_model, image_view):
        self.image_model = image_model
        self.image_view = image_view

        self.image = image_model.get_image_cv()

        U, S, V = svd(self.image)
        self.U = U
        self.S = S
        self.V = V
        # Get the size
        temp_image = self.image / 255
        self.original_size = str(temp_image.nbytes)

        # Get the k number
        max_k = min(self.image.shape)
        self.image_view.control.update_max_k(max_k)

        # Update the image size
        self.image_view.control.image_size_values.config(text='0/' + self.original_size)

        # Export the original image
        self.export_file(self.image, path.FILE_NAME)

        # Update the image
        self.image_view.display.set_image(self.cv2_to_pil(self.image_model.get_image_cv()))

        # Binding thingy
        self.image_view.control.compression_submit_button.bind("<Button-1>", self.submit_compression)
        self.image_view.control.back_button.bind("<Button-1>", self.back)
        self.image_view.control.export_button.bind("<Button-1>", self.export_compressed_file)

    def sum_size(self, array):
        return str(sum([matrix.nbytes for matrix in array]))

    def back(self, event):
        self.image_view.set_default()
        self.image_view.display.set_image(self.image_model.get_image_data())
        return True

    def cv2_to_pil(self, data):
        return Image.fromarray(data)

    def get_image_approximation(self, r):
        img_approx = self.U[:, :r] @ self.S[0:r, :r] @ self.V[:r, :]
        return img_approx, self.U[:, :r].astype('uint8'), self.S[0:r, :r].astype('uint8'), self.V[:r, :].astype('uint8')
    
    def get_loss(self, r):
        img_approx, U, S, V = self.get_image_approximation(r)
        max_intensity = np.max(self.image)
        mse = np.mean(np.square(self.image - img_approx))
        psnr = 20 * np.log10(max_intensity / np.sqrt(mse))
        return psnr
    
    def submit_compression(self, event):
        # Get the k number from the slider
        r = self.image_view.control.compression_rate_slider.get()

        # Get the image approximation
        img_approx, new_U, new_S, new_V = self.get_image_approximation(r)

        # Update the image size
        self.image_view.control.image_size_values.config(text=self.sum_size([new_U, new_S, new_V]) + '/' + self.original_size)

        # Update the image loss
        loss = self.get_loss(r)
        self.image_view.control.distance_values.config(text=str(loss))

        # Update the image
        # Add the compress image next to the original image
        new_image = np.hstack((self.image, img_approx))

        # Convert the image to PIL format
        new_image = self.cv2_to_pil(new_image)
        self.image_view.display.set_image(new_image)

    def export_file(self, data, file_name):
        save_path = path.OUTPUT + file_name + '.jpeg'
        cv2.imwrite(save_path, data)

        return True
    
    def export_compressed_file(self, event):
        r = self.image_view.control.compression_rate_slider.get()
        img_approx, U, S, V = self.get_image_approximation(r)
        img_approx = np.clip(img_approx, 0, 255).astype('uint8')
        self.export_file(img_approx, path.FILE_NAME + path.FILE_SVD_SUFFIX + str(r))

        return True