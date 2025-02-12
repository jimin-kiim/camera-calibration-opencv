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
            # ximagesource"
            # ximagesink: video frame into XWindow local/remote display    
# # gst-launch-1.0: build and run GStreamer pipeline. 
# icamerasrc: option for source file and in this case, it's for icamera, use 'icamersrc'
# video/x-raw: unstructured and uncompressed raw video data. else: x-ffv, x-h263, x-huffyuv .... etc.     
# # print-fps : ** couldn't find that where the value is printed. -> deleted      
# video convert : one of GstVideo Convert Scale (video convert, video convert scale, video scale)

# cap = cv.VideoCapture(1) -> [ WARN:0@982.602] global cap_v4l.cpp:913 open VIDEOIO(V4L2:/dev/video1): can't open camera by index
cap = cv.VideoCapture(gstreamer_str, cv.CAP_GSTREAMER)


# cap.set(5, 30.0) # FPS
# cap.set(3, 1920) # WIDTH
# cap.set(4, 1080) # HEIGHT
print("FPS: ", cap.get(5))
print(cap.isOpened())                                                                                        
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=get#cv2.VideoCapture.get
# https://www.geeksforgeeks.org/python-assert-keyword/

# Define the codec and create VideoWriter object
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