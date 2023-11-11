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

        self.control = Control_View(self)
        self.control.place(relwidth=0.2, relheight=1)

        self.display = Image_View(self)
        self.display.place(relwidth=0.8, relheight=1, relx=0.2)

    def start(self):
        self.mainloop()