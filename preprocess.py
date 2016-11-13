from PIL import Image
import sys
import cv2
import numpy as np

TARGET_FRAME_SIZE = (800, 600)

def match_size(imgfile, dim1, dim2):
    """Image is the path to the file we want to open, stored as a string.
    If you want to pass in an image object, make sure it's in a format that agrees with PIL"""
    im = Image.open(imgfile)
    im.thumbnail(TARGET_FRAME_SIZE, Image.ANTIALIAS)
    im.save(imgfile)

def image_to_tensor(imgfile):
    im = cv2.imread(imgfile)
    RGB = [np.zeros((len(im), len(im[0]))),
           np.zeros((len(im), len(im[0]))),
           np.zeros((len(im), len(im[0])))]

    for i in range(3):
        for row in range(len(im)):
            for col in range(len(im[row])):
                matrix = RGB[i]
                matrix[row, col] = im[row, col][i]
    return RGB

if __name__ == "__main__":
    print(image_to_tensor(sys.argv[1]))
