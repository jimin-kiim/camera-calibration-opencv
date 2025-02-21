import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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
cv.imshow(imgname, img)
cv.waitKey(0)
cv.destroyAllWindows()

grayscaledimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayscaledimgtitle = imgname + " grayscaled"
cv.imshow(grayscaledimgtitle, grayscaledimg)
cv.waitKey(0)
cv.destroyAllWindows()

ret, corners = cv.findChessboardCorners(grayscaledimg, (L,W), None)
print("Are Chessboard corners detected:\n", ret, "\n")

if ret == True:
    objpoints.append(objp)

    corners2 = cv.cornerSubPix(grayscaledimg, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    # Draw and display the corners
    cv.drawChessboardCorners(img, (L, W), corners2, ret)
    window_name = imgpath + ' with corner'
    cv.imshow(window_name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()

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
    cv.imshow(window_name, dst)
    cv.waitKey(0)

    cv.destroyAllWindows()
    cv.waitKey(1000)