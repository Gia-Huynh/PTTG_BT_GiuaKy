import tkinter as tk

class SVD_Control_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="SVD")
        self.label.grid(row=0)

        # Tool
        # Slider for the compression rate
        self.compression_rate_label = tk.Label(self, text="Độ nén")
        self.compression_rate_label.grid(row=2)

        self.compression_rate_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.compression_rate_slider.grid(row=3)

        self.compression_submit_button = tk.Button(self, text="Xác nhận")
        self.compression_submit_button.grid(row=4)

        # Export compressed image
        self.export_button = tk.Button(self, text="Xuất ảnh")
        self.export_button.grid(row=10)

        # Information/result/status
        # Image size, before and after
        self.image_size_label = tk.Label(self, text="Kich thước hình ảnh")
        self.image_size_label.grid(row=6)

        self.image_size_values = tk.Label(self, text="0/0")
        self.image_size_values.grid(row=7)

        # Distance between original and compressed image
        self.distance_label = tk.Label(self, text="Độ đo")
        self.distance_label.grid(row=8)

        self.distance_values = tk.Label(self, text="0")
        self.distance_values.grid(row=9)

        # Go back button
        self.back_button = tk.Button(self, text="Quay lại")
        self.back_button.grid(row=12)

    def update_max_k(self, max_k):
        self.compression_rate_slider.config(to=max_k)
        return True