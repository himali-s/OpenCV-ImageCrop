import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
			
		#if q press close frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('output.png',frame)
            img = cv2.imread('output.png',0)
            cv2.imshow('image',img)
            px = img[100,100] #accessing pixel
            print(px)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()