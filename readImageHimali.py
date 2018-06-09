import numpy as np
import cv2
# just read the image and displays in cmd
img = cv2.imread('tiger.jpg',0)
print(img)
#displays a image of tiger
#"image " is the name of image
# waitKey will wait for any key to be pressed
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#display the pixels
# undistort
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)
