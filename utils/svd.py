import numpy as np
import cv2
import matplotlib.pyplot as plt 

def svd(A):
    
    ATA = np.dot(A.T, A)
    
    eigenvalues, V = np.linalg.eig(ATA)

    eigenvalues = np.abs(eigenvalues)

    singular_values = np.sqrt(eigenvalues)
    
    ncols = np.argsort(singular_values)[::-1]

    singular_values = singular_values[ncols]

    V = V[:, ncols]
    m, n = A.shape
    
    Sigma = np.zeros((m, n))

    Sigma = np.zeros((m, n))
    Sigma[:m, :n] = np.diag(singular_values)

        
    U = A.dot(V) / singular_values
    
    return U, Sigma, V.T

def visualize(img, r = 200):
    img = cv2.resize(img, (160, 160))
    U, S, V = svd(img)
    S = np.diag(S)
    # print(U, S ,V)
    img_approx = U[:, :r] @ S[0:r, :r] @ V[:r, :]

    return img_approx

if __name__ == "__main__":
    img = cv2.imread("test.jpg", 0)
    img = cv2.resize(img, (160, 160))
    U, S, V = svd(img)

    print(U, S ,V)
    fig, ax = plt.subplots(5, 2, figsize=(8, 20))
    
    curr_fig = 0
    for r in [5, 10, 70, 100, 200]:
        img_approx = U[:, :r] @ S[0:r, :r] @ V[:r, :]
        ax[curr_fig][0].imshow(img_approx, cmap='gray')
        ax[curr_fig][0].set_title("k = "+str(r))
        ax[curr_fig, 0].axis('off')
        ax[curr_fig][1].set_title("Original Image")
        ax[curr_fig][1].imshow(img, cmap='gray')
        ax[curr_fig, 1].axis('off')
        curr_fig += 1
    plt.show()
