import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

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

    def back(self, event):
        self.image_view.set_default()
        self.image_view.display.set_image(self.image_model.get_image_data())
        return True
