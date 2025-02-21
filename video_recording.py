import cv2 as cv
from datetime import datetime
import os
import sys


os.environ['GST_PLUGIN_PATH'] = '/lib/gstreamer-1.0:/lib/x86_64-linux-gnu/gstreamer-1.0'
print("GST_PLUGIN_PATH: ",os.environ['GST_PLUGIN_PATH'])

os.environ['cameraDebug'] = '0'
print("cameraDebug: ", os.environ['cameraDebug'])

print(sys.argv[1])
camera_name = sys.argv[1]

gstreamer_str = f"icamerasrc device-name=isx031-{camera_name} ! video/x-raw,format=UYVY,width=1920,height=1080,framerate=30/1 ! videoconvert ! appsink"

cap = cv.VideoCapture(gstreamer_str, cv.CAP_GSTREAMER)

print("FPS: ", cap.get(5))
print(cap.isOpened())                                                                                        
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=get#cv2.VideoCapture.get
# https://www.geeksforgeeks.org/python-assert-keyword/

fourcc = cv.VideoWriter_fourcc(*'mp4v')

now = datetime.now()                        

fname=datetime.now().strftime("%Y-%m-%d-%H%M%S") + f"-{camera_name}.mp4"
outputpath = "output/" + fname                                                                                                                                                                                                                                                                 
out = cv.VideoWriter(outputpath, fourcc, 30.0, (1920, 1080))
print(os.listdir("output"))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    out.write(frame)
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        cap.release()
        out.release()

        break