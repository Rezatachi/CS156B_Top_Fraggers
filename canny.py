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

def get_folder(folder):
    # get folder, just to test this function
    # ignore this function
    for root, dirs, files in os.walk(folder):
        if dirs != []:
            print(dirs)
        else:
            print(root)

def canny(folder, desired_path):
    os.chdir(folder)
    # actual hog work
    for root, directory, files in os.walk(folder):
        if directory == []:
            for file in files:
                d = direc + "/" if direc != [] else ""
                filename = root + "/" + d + file
                assert os.path.exists(filename)
                im = cv2.imread(filename)
                im = cv2.resize(im, (224,224))
                im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                im_gray = cv2.GaussianBlur(im_gray, (5,5), 0)
                _, threshold = cv2.threshold(im_gray, 130, 190, 0)
                edges = cv2.Canny(threshold, 100, 255)
                cv2.imwrite(file, edges)
                shutil.move(file, f"{desired_path}/{root}/{d}")
        else:
            for dirs in directory:
                for root, direc, files, in os.walk(dirs):
                    for file in files:
                        d = direc + "/" if direc != [] else ""
                        filename = root + "/" + d + file
                        assert os.path.exists(filename)
                        im = cv2.imread(filename)
                        im = cv2.resize(im, (224,224))
                        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        im_gray = cv2.GaussianBlur(im_gray, (5,5), 0)
                        _, threshold = cv2.threshold(im_gray, 130, 190, 0)
                        edges = cv2.Canny(threshold, 100, 255)
                        cv2.imwrite(file, edges)
                        shutil.move(file, f"{desired_path}/{root}/{d}")
                        

# make a new directory for train and test
canny_train_path = "canny-detecion-train"
canny_test_path = "canny-detecion-test"
os.mkdir(canny_train_path)
os.mkdir(canny_test_path)
# you can run these commands in your own workspace and use the images in your models.
folder_path_train = "/groups/CS156b/data/train"
folder_path_test = "/groups/CS156b/data/test"
canny(folder_path, hog_train_path)
canny(folderpath, hog_test_path)
