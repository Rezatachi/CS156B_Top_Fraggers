import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import cv2
import shutil
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
# test

def histogram_of_oriented_gradients(filename):
    im = cv2.imread(filename)
    # resize image
    im = cv2.resize(im, (224, 224))
    # convert to grayscale
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # creating HOG features
    fd, hog_image = hog(im_gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)
    # plot image
    plt.imshow(hog_image, cmap='gray')
    plt.show()
    return fd, hog_image

histogram_of_oriented_gradients('view2_frontal.jpg')
