import numpy as np
import cv2
import cv2.cv2
import time
import os
import random
import sys
from datetime import datetime
import imutils

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year


fps = 48
width = 640
height = 480
#video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")
video_codec = cv2.VideoWriter_fourcc(*'mp4v')
#video_codec = cv2.VideoWriter_fourcc(*'mp4v')
name = "Videos"
print(name)
backImage = cv2.imread("background.jpg")

if os.path.isdir(str(name)) is False:
    name = "Videos"
    name = os.path.join(os.getcwd(), str(name))
    print("ALl logs saved in dir:", name)
    os.mkdir(name)
else:
    name = "Videos"
    name = os.path.join(os.getcwd(), str(name))
    print("ALl logs saved in dir:", name)


cap = cv2.VideoCapture(0)
ret = cap.set(3, 640)
ret = cap.set(4, 480)
cap1 = cv2.VideoCapture(1)
ret = cap1.set(3, 640)
ret = cap1.set(4, 480)
cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


start = time.time()
video_file_name = "CAM_"+str(currentMonth)+str(currentDay)+str(currentHour)+str(currentMinute)+str(currentSecond)
video_file_1 = os.path.join(name, str(video_file_name) + ".mp4")


# Create a video write before entering the loop
video_writer = cv2.VideoWriter(
    video_file_1, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
)

while True:
    try:
        start_time = time.time()
        ret, frame = cap.read()
        ret, frame1 = cap1.read()


        path = name
        now = time.time()

        for filename in os.listdir(path):
            # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
            if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:        #7 * 86400
                if os.path.isfile(os.path.join(path, filename)):
                    print(filename)
                    os.remove(os.path.join(path, filename))

        timer =int(time.time() - start)
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        currentSecond = datetime.now().second
        currentMinute = datetime.now().minute
        currentHour = datetime.now().hour

        cv2.putText(frame,"CAM1 {}".format(str(timer)), (30, 30), cv2.cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, "{}:{}:{}".format(currentHour,currentMinute,currentSecond), (30, 60), cv2.cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame1, "CAM2 {}".format(str(timer)), (30, 30), cv2.cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame1, "{}:{}:{}".format(currentHour, currentMinute, currentSecond), (30, 60),cv2.cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        frameTotal = np.hstack([frame, frame1])
        frameRecord = imutils.resize(frameTotal,width=640)
        frameRecord = cv2.copyMakeBorder(frameRecord, 120, 120, 0, 0, cv2.BORDER_CONSTANT, None, value = 0)
        cv2.imshow("Camera ATT V1.0.1", frameRecord)

        if timer >300:
            start = time.time()
            video_file_name = "CAM_" + str(currentMonth) + str(currentDay) + str(currentHour) + str(currentMinute) + str(
                currentSecond)
            video_file = os.path.join(name, str(video_file_name) + ".mp4")


            video_writer = cv2.VideoWriter(
                video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
            )


        # Write the frame to the current video writer
        video_writer.write(frameRecord)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    except Exception as e:
        print(e)



    if cv2.waitKey(1) & 0xFF == ord("q"):

        break

cap.release()
cap1.release()
    
cv2.destroyAllWindows()