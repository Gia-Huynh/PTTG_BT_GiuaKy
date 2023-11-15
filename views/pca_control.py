import tkinter as tk

class PCA_Control_View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Add widgets here
        self.label = tk.Label(self, text="PCA")
        self.label.grid(row=0)

        # Tool
        # Slider for the compression rate
        self.submit_button = tk.Button(self, text="Thực hiện PCA")
        self.submit_button.grid(row=4)

        # Information/result/status
        # Image size, before and after
        self.image_size_label = tk.Label(self, text="Thông tin ở đây.")
        self.image_size_label.grid(row=6)

        # Distance between original and compressed image
        self.n_feature_label = tk.Label(self, text="Số đặc trưng")
        self.n_feature_label.grid(row=7)

        self.n_feature = tk.Label(self, text="0")
        self.n_feature.grid(row=8)

        self.predict_label = tk.Label(self, text="Kết quả")
        self.predict_label.grid(row=9)

        self.predict = tk.Label(self, text="0")
        self.predict.grid(row=10)

        # Go back button
        self.back_button = tk.Button(self, text="Quay lại")
        self.back_button.grid(row=12)

    def update_n_feature(self, max_k):
        self.n_feature.config(text=max_k)
        return True
    
    def update_predict(self, predict):
        self.predict.config(text=predict)
        return True