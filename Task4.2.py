import cv2 
image1 = cv2.imread("index2.jpg")
image1 = image1[0:159,0:300]
image1.shape
image2 = cv2.imread("index.jpg")
image2 = image2[0:159,0:300]
image2.shape
import numpy as np 
image1_image2_hori = np.hstack((image1,image2))


cv2.imshow("Horizontal",image1_image2_hori)
cv2.waitKey()
cv2.destroyAllWindows()
image1_image2_ver = np.vstack((image1,image2))
cv2.imshow("vertical-collage", image1_image2_ver)
cv2.waitKey()
cv2.destoryAllWindows()
