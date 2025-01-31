from time import time

import matplotlib.pyplot as plt
from scipy.stats import loguniform
import numpy as np
import cv2
from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

Num_Eigenface = 30
#100 in production
min_faces = 100
#70 in production
class EigenFace:
    def __init__(self):
        #self.name =  name
        #lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
        lfw_people = fetch_lfw_people(min_faces_per_person=min_faces)
        n_samples, h, w = lfw_people.images.shape
        X = lfw_people.data
        n_features = X.shape[1]
        y = lfw_people.target
        target_names = lfw_people.target_names
        n_classes = target_names.shape[0]

        print("Chi tiết Dataset:")
        print("Số lượng mẫu: %d" % n_samples)
        print("Số đặc trưng: %d" % n_features)
        print("Số lớp: %d" % n_classes)
        print ("Kích thước dataset:",X.shape,", h:",h,", w:",w)

        #Chia dataset đầu vào thành train và test, với 20% để test phần còn lại là train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=69)
        
        #Chuẩn hóa dataset đầu vào
        self.scaler = StandardScaler()
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        
        n_components = Num_Eigenface
        print("Lấy %d eigenfaces tốt nhất từ %d khuôn mặt" % (n_components, X_train.shape[0]))
        pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
        eigenfaces = pca.components_.reshape((n_components, h, w))
        #print("Projecting the input data on the eigenfaces orthonormal basis")
        print("Chuyển hệ cơ sở của dữ liệu đầu vào sang hệ cơ sở vuông góc eigenfaces")
        X_train_pca = pca.transform(X_train)
        X_test_pca = pca.transform(X_test)
        print("Fitting the classifier to the training set")
        print("Khớp hóa (fitting) mô hình dự đoán vào bộ dữ liệu huấn luyện")
        param_grid = {
            "C": loguniform(1e3, 1e5),
            "gamma": loguniform(1e-4, 1e-1),
        }
        clf = RandomizedSearchCV(
            SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
        )
        clf = clf.fit(X_train_pca, y_train)
        print("Mô hình tốt nhất tìm được dựa trên giải thuật tìm kiếm lưới (grid search):")
        print(clf.best_estimator_)
        print("Dự đoán bộ dữ liệu kiểm tra (test set):")
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=target_names))
        
        self.clf = clf
        self.pca = pca
        self.target_names = target_names
        self.eigenfaces = eigenfaces #shape: (Num_Eigenface, 62, 47)
            
    def GetFeatureVectors (self, imgPath):
        #Trả về vector đặc trưng, shape: (1, Num_Eigenface)
        img2D = np.mean(cv2.resize (cv2.imread (imgPath), (47, 62)), axis = 2)
        img1D = np.ravel (img2D).reshape(1, -1)
        img1D = self.scaler.transform(img1D)
        return self.pca.transform(img1D)
    
    def predict_img_path (self, imgPath):
        #Dự đoán ảnh đầu vào là class nào trong dataset huấn luyện.
        #Trả về tên của người được dự đoán.
        #inpImg: Greyscale, size: 62 x 47.
        img2D = np.mean(cv2.resize (cv2.imread (imgPath), (47, 62)), axis = 2)
        img1D = np.ravel (img2D).reshape(1, -1)
        img1D = self.scaler.transform(img1D)
        img1d_pca = self.pca.transform(img1D)
        result = self.clf.predict(img1d_pca)
        return self.target_names[result[0]].rsplit(" ", 1)[-1]
    
    def get_Eigenfaces_And_Feature (self, imgPath, num = 10):
        #Trả về: List chứa Num phần tử, mỗi phần tử thứ i chứa 2 thằng con,
        #Thằng con đầu là phần tử thứ i của vector đặc trưng, thằng 2 là mặt eigen của nó
        #Access: result[0][0] là một số float
        #result [0][1] có shape = (62, 47), đưa vào cv2 imshow thì chắc add axis
        
        #(1, 50)[0] = (50)
        FtVectors = self.GetFeatureVectors (imgPath)[0]
        result = []
        for i in range (num):
            result.append ([FtVectors[i], self.eigenfaces[i]])
        return result
    def predict_img_list (self, inpImg):
        pass
    
ey = EigenFace ()
result = ey.predict_img_path("lfw\\Aaron_Eckhart\\Aaron_Eckhart_0001.jpg")
print (result)
result2 = ey.GetFeatureVectors("lfw\\Aaron_Eckhart\\Aaron_Eckhart_0001.jpg")
print (result2)
result3 = ey.get_Eigenfaces_And_Feature("lfw\\Aaron_Eckhart\\Aaron_Eckhart_0001.jpg")
print (result3)
