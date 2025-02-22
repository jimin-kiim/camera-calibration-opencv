import cv2 as cv
import numpy as np

termiation_criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

chessboard_width = 7
chessboard_length = 10 

objp = np.zeros((chessboard_width * chessboard_length, 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboard_length, 0:chessboard_width].T.reshape(-1, 2)

realworldpoints = []
imgpoints = []

videofilename = "2025-02-11-111507-h-3.mp4"
videopath = f'input/{videofilename}'
cap = cv.VideoCapture(videopath)
if not cap:
    print("Error occured while instantiating Video Capture")

idx = 0
while (cap.isOpened()):
    isframeavailable, frame = cap.read()

    if isframeavailable != True:
        print("Fetching Frame ended in INDEX: ", idx)
        break
    idx += 1

    grayscaledimg = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    patternfound, corners = cv.findChessboardCorners(grayscaledimg, (chessboard_length, chessboard_width), None)
    if idx % 50 == 0: print(f"chesssboard pattern of {idx}th frame has been found:", patternfound) 

    if patternfound:
        realworldpoints.append(objp)
    
        corners2 = cv.cornerSubPix(grayscaledimg, corners, (11,11), (-1,-1), termiation_criteria)
        imgpoints.append(corners2)

        cv.drawChessboardCorners(frame, (chessboard_length, chessboard_width), corners2, patternfound)

print("\nCalibrating the Camera matrix and distortion coefficient\n")
iscalibrated, mtx, dist, rvecs, tvecs = cv.calibrateCamera(realworldpoints, imgpoints, grayscaledimg.shape[::-1], None, None)

if iscalibrated:
    print("Calibration is successfully done.")
    print("Camera Matrix: \n", mtx, "\n")
    print("Distortion Coefficient: \n", dist, "\n")
else:
    print("Calibration failed")

cap.release()