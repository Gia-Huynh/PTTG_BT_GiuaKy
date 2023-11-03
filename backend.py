import numpy
import matplotlib
import cv2, glob, tkinter
def loadImage (path, *arg):
    image = cv2.imread (path)
    return image

def loadImages (path, *arg):
    arrImage = []
    for file in glob.glob (path + "*.*"):
        image = cv2.imread (path)
        arrImage.append (image)
    return arrImage

def PCA (image):
    array_reduced = image
    return array_reduced
def SVD (image):
    heatmap_image = image
    return heatmap_image
