import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import cv2
import shutil
# test

def get_folder(folder):
    # get folder, just to test this function
    # ignore this function
    for root, dirs, files in os.walk(folder):
        if dirs != []:
            print(dirs)
        else:
            print(root)

def blob(folder, desired_path):
    # actual blob detection, used gaussian blur first to get the best results
    for root, dirs, files in os.walk(folder):
        if dirs == []:
            for file in files:
                im = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
                im = cv2.resize(im, (224, 224))
                im = cv2.GaussianBlur(im, (5, 5), 0)
                detector = cv2.SimpleBlobDetector_create()
                keypoints = detector.detect(im)
                im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                cv2.imwrite(file, im_with_keypoints)
                shutil.move(file, f"{desired_path}{root}")
        else:
            for dires in dirs:
                for root, dirs, files, in os.walk(dires):
                    for file in files:
                        im = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
                        im = cv2.resize(im, (224, 224))
                        im = cv2.GaussianBlur(im, (5, 5), 0)
                        detector = cv2.SimpleBlobDetector_create()
                        keypoints = detector.detect(im)
                        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                        cv2.imwrite(file, im_with_keypoints)
                        shutil.move(file, f"{desired_path}{root}{dires}")

# make a new directory for train
blob_train_path = "/groups/CS156b/data/blob-detecion-train"
blob_test_path = "/groups/CS156b/data/blob-detecion-test"
# os.mkdir(blob_train_path)
# os.mkdir(blob_test_path)
folder_path = "/groups/CS156b/data/train"
# get_folder(folder_path)
# blob(folderpath, blob_train_path)
# blob(folderpath, blob_test_path)
