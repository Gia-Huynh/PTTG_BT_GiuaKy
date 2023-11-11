import numpy as np
import cv2
import matplotlib.pyplot as plt 

from utils.svd import svd

class SVD_Controller:
    def __init__(self, image):
        self.image = image

        U, S, V = svd(image)
        self.U = U
        self.S = S
        self.V = V
        
    def get_image_approximation(self, r):
        img_approx = self.U[:, :r] @ self.S[0:r, :r] @ self.V[:r, :]
        return img_approx
    
    def get_loss(self, r):
        img_approx = self.get_image_approximation(r)
        loss = np.sum(np.square(self.image - img_approx))
        return loss
    
    