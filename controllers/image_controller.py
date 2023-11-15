import tkinter.filedialog # Temporary fix for import error
import tkinter as tk
from PIL import Image, ImageTk

from controllers.svd_controller import SVD_Controller
from controllers.pca_controller import PCA_Controller
from utils.EigenFace import EigenFace

class Image_Controller:
    def __init__(self, image_model, image_view):
        self.image_model = image_model
        self.image_view = image_view
        self.image_control = image_view.control
        self.image_display = image_view.display

        # Binding thingy
        self.image_control.upload_button.bind("<Button-1>", self.upload_image)
        self.image_control.reset_button.bind("<Button-1>", self.reset)
        self.image_control.svd_button.bind("<Button-1>", self.svd_triggered)
        self.image_control.pca_button.bind("<Button-1>", self.pca_triggered)

        # Other
        self.eigen_face = EigenFace()

    def upload_image(self, event):
        image_path = tk.filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp *.tiff *.tif *.jfif *.ico *.eps *.raw *.cr2 *.nef *.orf *.sr2 *.webp *.heif *.heic *.svg *.ai *.eps *.ps *.psd *.svgz *.wmf *.emf *.jfif *.jpe *.jpeg *.jif *.jfi")])
        if image_path:
            self.image_model.set_image_path(image_path)
            try:
                image_data = self.image_model.get_image_data()
                image = ImageTk.PhotoImage(image_data)
            except:
                # Add error message
                self.image_model.reset()
                return False
            finally:
                pass

            self.image_display.label.config(image=image)
            self.image_display.label.image = image

        return True

    def reset(self, event):
        self.image_model.reset()
        self.image_display.label.config(image=None)
        self.image_display.label.image = None
        return True
    
    def svd_triggered(self, event):
        if self.image_model.get_image_cv() is not None:
            self.image_view.set_svd()
            self.svd_controller = SVD_Controller(self.image_model, self.image_view)
        return True
    
    def pca_triggered(self, event):
        if self.image_model.get_image_cv() is not None:
            self.image_view.set_pca()
            self.svd_controller = PCA_Controller(self.image_model, self.image_view, self.eigen_face)
        return True