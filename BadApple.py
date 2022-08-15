import os
import shutil
import cv2

frames = []
video = cv2.VideoCapture(r"badapple.mp4")
success, image = video.read()

while success:
    frames.append(image)
    success,image = video.read()

cv2.imwrite("frame2.jpg", frames[100])
