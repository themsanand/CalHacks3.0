from PIL import Image
import random
import os
import subprocess
import sys
import cv2
import numpy as np

TARGET_FRAME_SIZE = (800, 600)

def match_size(imgfile):
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

def random_frame_from_video(video_path, out_prefix):
    vidlen = str(subprocess.check_output("ffmpeg -i {}  2>&1 | grep Duration | cut -d ' ' -f 4 | sed 's/,//'".format(video_path), shell=True), "utf-8")[:-1]
    print(vidlen)
    # vidlen comes out as a string hours:minutes:seconds
    # as int:int:float
    total_time = _to_int(vidlen)
    rand_time = _to_str(random.randint(0, int(total_time)))
    os.system('ffmpeg -ss {} -i {} -frames:v 1 {}.jpg'.format(rand_time, video_path, out_prefix))


def _to_int(vid_time):
    nums = vid_time.split(":")
    return int(nums[0]) * 3600 + int(nums[1]) * 60 + float(nums[2])

def _to_str(vid_int):
    return "{}:{}:{}".format(vid_int // 3600, (vid_int % 3600) // 60, float(vid_int % 60))

if __name__ == "__main__":
    #print(image_to_tensor(sys.argv[1]))
    #print(random_frame_from_video(sys.argv[1], "out"))
    #print(match_size(sys.argv[1]))
