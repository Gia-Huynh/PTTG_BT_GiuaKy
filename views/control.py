import tkinter as tk

class Control_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="Control")
        self.label.grid(row=0, column=0, columnspan=2)

        # Button for image
        self.upload_button = tk.Button(self, text="Upload Image")
        self.upload_button.grid(row=2, column=0, columnspan=2)

        self.reset_button = tk.Button(self, text="Reset image")
        self.reset_button.grid(row=3, column=0, columnspan=2)

        # Button for the 2 windows
        self.pca_button = tk.Button(self, text="PCA")
        self.pca_button.grid(row=5, column=0, columnspan=1, sticky='w')
        
        self.svd_button = tk.Button(self, text="SVD")
        self.svd_button.grid(row=5, column=1, columnspan=2, sticky='e')