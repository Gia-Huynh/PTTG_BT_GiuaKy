from tkinter import Tk

from views.control import Control_View
from views.svd_control import SVD_Control_View
from views.image import Image_View
from utils.screen_status import Screen

class Root(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(False, False)
        self.title("Main program")

        self.screen_status = Screen.DEFAULT

        self.control = Control_View(self)
        self.control.place(relwidth=0.2, relheight=1)

        self.display = Image_View(self)
        self.display.place(relwidth=0.8, relheight=1, relx=0.2)

    def set_svd(self):
        self.screen_status = Screen.SVD
        self.control.destroy()
        self.control = SVD_Control_View(self)
        self.control.place(relwidth=0.2, relheight=1)

    def set_pca(self):
        self.screen_status = Screen.PCA

    def set_default(self):
        self.screen_status = Screen.DEFAULT
        self.control.destroy()
        self.control = Control_View(self)
        self.control.place(relwidth=0.2, relheight=1)

    def start(self):
        self.mainloop()