import numpy as np
import cv2
import time
import os
import random
import sys
from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


fps = 369
width = 864
height = 640
video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

name = str(currentYear)+str(currentMonth)+str(currentDay)+str(currentHour)+str(currentMinute)+str(currentSecond)
print(name)
if os.path.isdir(str(name)) is False:
    name = str(currentYear)+str(currentMonth)+str(currentDay)+str(currentHour)+str(currentMinute)+str(currentSecond)
    name = str(name)

name = os.path.join(os.getcwd(), str(name))
print("ALl logs saved in dir:", name)
os.mkdir(name)


cap = cv2.VideoCapture(0)
ret = cap.set(3, 864)
ret = cap.set(4, 480)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


start = time.time()
video_file_name = str(currentHour)+str(currentMinute)+str(currentSecond)
video_file = os.path.join(name, str(video_file_name) + ".avi")
print("Capture video saved location : {}".format(video_file))

# Create a video write before entering the loop
video_writer = cv2.VideoWriter(
    video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
)

while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Action Camera", frame)
        if time.time() - start >600:
            start = time.time()
            currentSecond = datetime.now().second
            currentMinute = datetime.now().minute
            currentHour = datetime.now().hour

            video_file_name = str(currentHour) + str(currentMinute) + str(currentSecond)

            video_file = os.path.join(name, str(video_file_name) + ".avi")
            video_writer = cv2.VideoWriter(
                video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
            )
            # No sleeping! We don't want to sleep, we want to write
            # time.sleep(10)

        # Write the frame to the current video writer
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()