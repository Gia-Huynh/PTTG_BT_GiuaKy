import tkinter as tk

class PCA_Control_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="PCA")
        self.label.grid(row=0)

        # Tool
        # Slider for the compression rate
        self.pca_submit_button = tk.Button(self, text="Thực hiện PCA")
        self.pca_submit_button.grid(row=4)

        # Information/result/status
        # Image size, before and after
        self.image_size_label = tk.Label(self, text="Thông tin ở đây.")
        self.image_size_label.grid(row=6)

        # self.image_size_values = tk.Label(self, text="0/0")
        # self.image_size_values.grid(row=7)

        # # Distance between original and compressed image
        # self.distance_label = tk.Label(self, text="Distance")
        # self.distance_label.grid(row=8)

        # self.distance_values = tk.Label(self, text="0")
        # self.distance_values.grid(row=9)

        # # Export compressed image
        # self.export_button = tk.Button(self, text="Export")
        # self.export_button.grid(row=10)

        # Go back button
        self.back_button = tk.Button(self, text="Back")
        self.back_button.grid(row=12)

    # def update_max_k(self, max_k):
    #     self.compression_rate_slider.config(to=max_k)
    #     return True