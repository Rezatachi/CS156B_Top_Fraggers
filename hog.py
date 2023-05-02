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

def hog(folder, desired_path):
    os.chdir(folder)
    # actual hog work
    for root, directory, files in os.walk(folder):
        if directory == []:
            for file in files:
                d = direc + "/" if direc != [] else ""
                filename = root + "/" + d + file
                assert os.path.exists(filename)
                im = cv2.imread(filename)
                # resize image
                im = cv2.resize(im, (224, 224))
                # convert to grayscale
                im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                # creating HOG features
                fd, hog_image = hog(im_gray)
                cv2.imwrite(file, hog_image)
                shutil.move(file, f"{desired_path}/{root}/{d}")
        else:
            for dirs in directory:
                for root, direc, files, in os.walk(dirs):
                    for file in files:
                        d = direc + "/" if direc != [] else ""
                        filename = root + "/" + d + file
                        assert os.path.exists(filename)
                        im = cv2.imread(filename)
                        # resize image
                        im = cv2.resize(im, (224, 224))
                        # convert to grayscale
                        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                        # creating HOG features
                        _, hog_image = hog(im_gray, visualize=True)
                        cv2.imwrite(file, hog_image)
                        shutil.move(file, f"{desired_path}/{root}/{d}")
                        

# make a new directory for train and test
# if we still want to use HOGs, realzie that mkdir (for some reason) cannot be utilized in the /groups/CS156b/.. directory
hog_train_path = "hog-detecion-train"
hog_test_path = "hog-detecion-test"
os.mkdir(hog_train_path)
os.mkdir(hog_test_path)
# you can run these commands in your own workspace and use the images in your models.
folder_path_train = "/groups/CS156b/data/train"
folder_path_test = "/groups/CS156b/data/test"
hog(folder_path, hog_train_path)
hog(folderpath, hog_test_path)
