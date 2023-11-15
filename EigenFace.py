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

Num_Eigenface = 100
class EigenFace:
    def __init__(self):
        #self.name =  name
        #lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
        lfw_people = fetch_lfw_people(min_faces_per_person=70)
        n_samples, h, w = lfw_people.images.shape
        X = lfw_people.data
        n_features = X.shape[1]
        y = lfw_people.target
        target_names = lfw_people.target_names
        n_classes = target_names.shape[0]

        print("Total dataset size:")
        print ("Dataset Shape:",X.shape,", h:",h,", w:",w)
        print("n_samples: %d" % n_samples)
        print("n_features: %d" % n_features)
        print("n_classes: %d" % n_classes)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20, random_state=69)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        n_components = Num_Eigenface
        #150
        print(
            "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
        )
        t0 = time()
        pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
        print("done in %0.3fs" % (time() - t0))
        eigenfaces = pca.components_.reshape((n_components, h, w))
        print("Projecting the input data on the eigenfaces orthonormal basis")
        t0 = time()
        X_train_pca = pca.transform(X_train)
        X_test_pca = pca.transform(X_test)
        print("done in %0.3fs" % (time() - t0))
        print("Fitting the classifier to the training set")
        t0 = time()
        param_grid = {
            "C": loguniform(1e3, 1e5),
            "gamma": loguniform(1e-4, 1e-1),
        }
        clf = RandomizedSearchCV(
            SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
        )
        clf = clf.fit(X_train_pca, y_train)
        print("done in %0.3fs" % (time() - t0))
        print("Best estimator found by grid search:")
        print(clf.best_estimator_)
        print("Predicting people's names on the test set")
        t0 = time()
        y_pred = clf.predict(X_test_pca)
        print("done in %0.3fs" % (time() - t0))
        print(classification_report(y_test, y_pred, target_names=target_names))
        #ConfusionMatrixDisplay.from_estimator(
        #    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
        #)
        #plt.tight_layout()
        #plt.show()
        self.clf = clf
        self.pca = pca
        self.target_names = target_names
        self.eigenfaces = eigenfaces
    def title(y_pred, y_test, target_names, i):
        pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
        true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
        return "predicted: %s\ntrue:      %s" % (pred_name, true_name)
    def predict_img_path (self, imgPath):
        #inpImg: Greyscale, size: 62 x 47
        #"lfw\\Aaron_Eckhart\\Aaron_Eckhart_0001.jpg"
        #.reshape(-1, 1)
        img2D = np.mean(cv2.resize (cv2.imread (imgPath), (47, 62)), axis = 2)
        img1D = np.ravel (img2D).reshape(1, -1)
        img1d_pca = self.pca.transform(img1D)
        result = self.clf.predict(img1d_pca)
        return result
    def predict_img_list (self, inpImg):
        pass
ey = EigenFace ()
"""def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    #Helper function to plot a gallery of portraits
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())
        #



prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w)
eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

plt.show()"""
