from tkinter import Tk

from views.control import Control_View
from views.svd_control import SVD_Control_View
from views.pca_control import PCA_Control_View
from views.image import Image_View
from utils.screen_status import Screen

class Root(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(False, False)
        self.title("Main program")

        self.screen_status = Screen.DEFAULT

        # Store the control
        self.controls = {
            Screen.DEFAULT: Control_View(self),
            Screen.SVD: SVD_Control_View(self),
            Screen.PCA: PCA_Control_View(self),
        }

        for control in self.controls.values():
            if control is not None:
                control.place(relwidth=0.2, relheight=1)

        self.update_control()

        self.display = Image_View(self)
        self.display.place(relwidth=0.8, relheight=1, relx=0.2)

    def set_svd(self):
        self.screen_status = Screen.SVD
        self.update_control()

    def set_pca(self):
        self.screen_status = Screen.PCA
        self.update_control()

    def set_default(self):
        self.screen_status = Screen.DEFAULT
        self.update_control()

    def update_control(self):
        self.control = self.controls[self.screen_status]
        self.control.tkraise()

    def start(self):
        self.mainloop()