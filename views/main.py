from .root import Root

class View:
    def __init__(self):
        self.root = Root()

    def start(self):
        self.root.mainloop()