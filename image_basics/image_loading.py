# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 1 - Image Loading & Conversion ========== #

# ========== Part 1: (Load an image using python and display the image) ========== #

# Code to import cv2 
import cv2

# Code to load the image
image = cv2.imread("Colosseum.JPG")

# Code to allow resizing of the display window
cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)

# Code to display the image
cv2.imshow("Loaded Image", image)

# Code for closing window when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
