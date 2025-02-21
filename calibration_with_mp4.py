import cv2 as cv
import numpy as np

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

W = 7
L = 10 

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((W*L, 3), np.float32)
objp[:,:2] = np.mgrid[0:L, 0:W].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

videopath = 'input/2025-02-11-111507-h-3.mp4'
cap = cv.VideoCapture(videopath) # capturing a video file. after capturing -> can read the frames one by one.
print(cap)
# value of the constants: https://docs.opencv.org/4.3.0/d4/d15/group__videoio__flags__base.html ;  stored using enum. 

idx = 0
while (cap.isOpened()):
    isframeavailable, frame = cap.read()  # read the next frame of the video. 
    # print("Frame available exist:", ret)
    if isframeavailable != True:
        print("Fetching Frame ended in INDEX: ", idx)
        break
    idx += 1

    grayscaledimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
    # Find the chess board corners
    patternfound, corners = cv.findChessboardCorners(grayscaledimg, (L, W), None)
    if idx % 50 == 0: print(f"chesssboard pattern of {idx}th frame has been found:", patternfound) 

    if patternfound:
        objpoints.append(objp)
    
        corners2 = cv.cornerSubPix(grayscaledimg, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
    
        # Draw and display the corners
        cv.drawChessboardCorners(frame, (L, W), corners2, patternfound)

print("\nCalibrating the Camera matrix and distortion coefficient\n")
iscalibrated, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, grayscaledimg.shape[::-1], None, None)

if iscalibrated:
    print("Calibration is successfully done.")
    print("Camera Matrix: \n", mtx, "\n")
    print("Distortion Coefficient: \n", dist, "\n")
else:
    print("Calibration failed")

cap.release() # closing a video file

