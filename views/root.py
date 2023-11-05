from tkinter import Tk

from constant import window
from views.control import Control_View
from views.image import Image_View

class Root(Tk):
    def __init__(self):
        super().__init__()

        start_width = window.WIDTH
        min_width = window.MIN_WIDTH
        start_height = window.HEIGHT
        min_height = window.MIN_HEIGHT

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("Something something")

        # The control frame is 0.8 height and 0.3 width of the root frame
        self.control = Control_View(self)
        self.control.place(relwidth=0.2, relheight=1)

        # The image frame is 0.8 height and 0.7 width of the root frame
        self.image = Image_View(self)
        self.image.place(relwidth=0.8, relheight=1, relx=0.2)

    def set_image_callback(self, callback):
        self.control.set_image_callback(callback)

    def update_image(self, image):
        self.image.set_image(image)

    def start(self):
        self.mainloop()