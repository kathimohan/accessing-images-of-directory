
import numpy as np
import argparse
import cv2
import os
import cvlib as cv
import time


def ca(dir):
    for path,subdirnames,filenames in os.walk(dir, topdown=False):
        print(path)
        print(subdirnames)
        print(filenames)
        for filename in filenames:
            print(filename)
            img_path=os.path.join(path,filename)
            print(img_path)

ca('images')

