from tkinter import Tk

from constant import window
from views.control import Control
from views.image import Image

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
        self.control = Control(self)
        self.control.place(relheight=0.8, relwidth=0.2)

        # The image frame is 0.8 height and 0.7 width of the root frame
        self.image = Image(self)
        self.image.place(relheight=0.8, relwidth=0.8, relx=0.2)