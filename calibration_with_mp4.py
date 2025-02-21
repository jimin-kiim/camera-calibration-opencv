import cv2 as cv
import numpy as np

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

W = 7
L = 10 

objp = np.zeros((W*L, 3), np.float32)
objp[:,:2] = np.mgrid[0:L, 0:W].T.reshape(-1, 2)

objpoints = []
imgpoints = []

videopath = 'input/2025-02-11-111507-h-3.mp4'
cap = cv.VideoCapture(videopath)
print(cap)
# value of the constants: https://docs.opencv.org/4.3.0/d4/d15/group__videoio__flags__base.html ;  stored using enum. 

idx = 0
while (cap.isOpened()):
    isframeavailable, frame = cap.read()
    if isframeavailable != True:
        print("Fetching Frame ended in INDEX: ", idx)
        break
    idx += 1

    grayscaledimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
    patternfound, corners = cv.findChessboardCorners(grayscaledimg, (L, W), None)
    if idx % 50 == 0: print(f"chesssboard pattern of {idx}th frame has been found:", patternfound) 

    if patternfound:
        objpoints.append(objp)
    
        corners2 = cv.cornerSubPix(grayscaledimg, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
    
        cv.drawChessboardCorners(frame, (L, W), corners2, patternfound)

print("\nCalibrating the Camera matrix and distortion coefficient\n")
iscalibrated, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, grayscaledimg.shape[::-1], None, None)

if iscalibrated:
    print("Calibration is successfully done.")
    print("Camera Matrix: \n", mtx, "\n")
    print("Distortion Coefficient: \n", dist, "\n")
else:
    print("Calibration failed")

cap.release()

