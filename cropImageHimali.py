#import numpy as np
import cv2

if __name__ == '__main__' :
 
    # Read image
    im = cv2.imread("output.png")
     
    # Select ROI
    r = cv2.selectROI(im)
     
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imwrite('croppedImage.png',imCrop)
 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    print(imCrop.size)
    #accessing red pixel value
    print(imCrop.item(10,10,2))
    #modifying pixel
    imCrop[100,100] = [255,255,255]
    print(imCrop[100,100])
    image = cv2.resize(imCrop, (640, 480), 0, 0, cv2.INTER_NEAREST)
    cv2.waitKey(0)
