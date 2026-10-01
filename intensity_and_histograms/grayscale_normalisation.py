# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# Question 4 - Intensity Range Adjustment & Histogram Equalisation

# ========== Part 2: (Convert the colour image to grayscale and display in its full intensity range [0,255]) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the original image
image = cv2.imread("peppers.png")

# Code to convert image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Code to normalize intensity range to [0,255]
gray_normalized = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)

# Code to display the seperate images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_normalized)

# Code to close all windows if a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
