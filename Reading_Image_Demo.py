# Python code to reading an image using OpenCV

import numpy as np
import cv2
# You can give path to the
# image as first argument
img = cv2.imread('Animal.jpg', 1)

# will show the image in a window
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
#0xFF is a hexadecimal constant which is 11111111 in binary.


#wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('Animal.jpg',img)
    cv2.destroyAllWindows()

