import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def showimg(windowname, img, atthelast = False):
    cv.imshow(windowname, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    if atthelast:
        cv.waitKey(1000)


criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

W = 23
L = 31

objp = np.zeros((W*L, 3), np.float32)
objp[:,:2] = np.mgrid[0:L,0:W].T.reshape(-1,2)

objpoints = [] 
imgpoints = [] 

imgname = 'camera_calib5.jpg'
imgpath = f'images/{imgname}'


img = cv.imread(imgpath)
showimg(imgname, img)

grayscaledimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayscaledimgtitle = imgname + " grayscaled"
showimg(grayscaledimgtitle, grayscaledimg)

ret, corners = cv.findChessboardCorners(grayscaledimg, (L,W), None)
print("Are Chessboard corners detected:\n", ret, "\n")

if ret:
    objpoints.append(objp)

    corners2 = cv.cornerSubPix(grayscaledimg, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    cv.drawChessboardCorners(img, (L, W), corners2, ret)
    window_name = imgpath + ' with corner'
    showimg(window_name, img)

    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, grayscaledimg.shape[::-1], None, None)
    print(ret)
    print("Camera Matrix:\n", mtx, "\n")
    print("Distortion Coefficient:\n", dist, "\n")
    print(rvecs, "\n", tvecs)

    h,  w = grayscaledimg.shape[:2]
    newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

    dst = cv.undistort(grayscaledimg, mtx, dist, None, newcameramtx)
    
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
    outputpath = f"output/{imgname}"
    showimg(window_name, dst, True)