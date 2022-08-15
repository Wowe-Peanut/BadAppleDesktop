import os
import shutil
import cv2


#Never call again lol
def parse_frames:
  video = cv2.VideoCapture('badapple.mp4')
  success,image = video.read()
  count = 0
  
  while success:
    cv2.imwrite(r"C:\Users\Peanu\OneDrive\Desktop\BadAppleDesktop\frames\frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = video.read()
    count += 1





