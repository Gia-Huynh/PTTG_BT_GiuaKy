import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

class PCA_Controller:
    def __init__(self, image_model, image_view, eigen_face):
        self.image_model = image_model
        self.image_view = image_view

        self.pca = eigen_face
        self.n_feature = self.pca.n_features

        # Init things here
        self.image_view.control.update_n_feature(self.n_feature)

        # Binding thingy
        self.image_view.control.back_button.bind("<Button-1>", self.back)
        self.image_view.control.submit_button.bind("<Button-1>", self.submit_pca)

    def submit_pca(self, event):
        predict = self.pca.predict_img_path(self.image_model.get_image_path())
        self.image_view.control.update_predict(predict)

        eigenface = self.pca.get_Eigenfaces_And_Feature(self.image_model.get_image_path())
        n = len(eigenface)
        eigenface_1 = eigenface[0][1]
        eigenface_2 = eigenface[5][1]
        for i in range(1, 5):
            eigenface_1 = np.hstack((eigenface_1, eigenface[i][1]))
        for i in range(6, n):
            eigenface_2 = np.hstack((eigenface_2, eigenface[i][1]))
        new_eigenface = np.vstack((eigenface_1, eigenface_2))
        new_eigenface = self.normalized(new_eigenface)
        original_image = self.image_model.get_image_cv()
        new_height = int(original_image.shape[0] * new_eigenface.shape[1] / original_image.shape[1])
        new_eigenface = cv2.resize(new_eigenface, (original_image.shape[1], new_height))
        new_eigenface = np.vstack((original_image, new_eigenface))

        image = Image.fromarray(new_eigenface)
        self.image_view.display.set_image(image)

        values = [eigenface[i][0] for i in range(n)]
        print(values)

    def normalized(self, img):
        img = img.astype(np.float32)
        img = (img - np.min(img)) / (np.max(img) - np.min(img))
        img = img * 255
        img = img.astype(np.uint8)
        return img

    def back(self, event):
        self.image_view.set_default()
        self.image_view.display.set_image(self.image_model.get_image_data())
        return True
