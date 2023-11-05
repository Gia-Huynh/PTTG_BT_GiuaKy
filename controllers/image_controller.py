import tkinter.filedialog # Temporary fix for import error
import tkinter as tk

class Image_Controller:
    def __init__(self, image_model, image_view):
        self.image_model = image_model
        self.image_view = image_view

        self.image_view.set_image_callback(self.upload_image)

    def upload_image(self):
        image_path = tk.filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp *.tiff *.tif *.jfif *.ico *.eps *.raw *.cr2 *.nef *.orf *.sr2 *.webp *.heif *.heic *.svg *.ai *.eps *.ps *.psd *.svgz *.wmf *.emf *.jfif *.jpe *.jpeg *.jif *.jfi")])
        if image_path:
            self.image_model.set_image_path(image_path)
            self.image_view.update_image(self.image_model.get_image_data())