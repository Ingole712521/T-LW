import cv2
import numpy as np


def create_blank(width, height, rgb_color=(0, 0, 0)):
    
    image = np.zeros((height, width, 3), np.uint8)

   
    color = tuple(reversed(rgb_color))
    image[:] = color

    return image


# Create new blank 300x300 red image
width1, height1 = 300, 300

red = (255, 0, 0)
image = create_blank(width1, height1, rgb_color=red)
cv2.imshow("Blank Image", image)
cv2.imwrite('red.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
