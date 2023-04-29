import os 
import numpy as np
import matplotlib.pyplot as plt
import cv2
import shutil
import pandas as pd

def demo_canny_test(filename):
    im = cv2.imread(filename=filename)
    im = cv2.resize(im, (224,224))
    # convert to grayscale and add gauss
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # gauss = cv2.GaussianBlur(im_gray, (5, 5), 0)
    # locate a threshold
    _, threshold = cv2.threshold(im_gray, 130, 190, 0)
    # edges = cv2.Canny(threshold, 100, 255)
    plt.figure()
    plt.imshow(threshold, cmap="gray"), #plt.xticks([]), plt.yticks([])  


    plt.show()

demo_canny_test("view3_frontal.jpg")