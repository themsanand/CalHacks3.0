from getvideo import *
from getgif import *
from preprocess import *
import os
import sys
import random

def twoframes():
    paths = ["video-1479037873.mp4",
             "video-1479037934.mp4",
             "video-1479037987.mp4"]
    i1 = random.randint(0, len(paths)-1)
    video_path = paths[i1]
    t1 = random_frame_from_video(video_path, 'out1')
    if random.randint(0,2):
        del paths[i1]
        i1 = random.randint(0, len(paths)-1)
    video_path = paths[i1]
    t2 = random_frame_from_video(video_path, 'out2')
    return t2 - t1

if __name__ == "__main__": # I don't know why you'd be here otherwise.
    print(twoframes())
