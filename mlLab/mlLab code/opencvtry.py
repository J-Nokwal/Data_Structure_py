import numpy as np
import cv2
arr=np.zeros((100,100,3))
arr[:]=225,0,0

cv2.imshow("image",arr)

cv2.waitKey()