import tkinter as tk

class Control(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="Control")
        self.label.pack()

        self.buttons = []

        # Generate a bunch of buttons for placeholder
        for i in range(10):
            button = tk.Button(self, text=f"Button {i}")
            self.buttons.append(button)
            self.buttons[i].pack(side=tk.TOP, fill=tk.X)
        
