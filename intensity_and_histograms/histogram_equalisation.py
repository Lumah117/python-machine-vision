# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 4 - Intensity Range Adjustment & Histogram Equalisation ========== #

# ========== Part 4: (Apply histogram equalisation to the grayscale image and compare it to the original grayscale image) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Cde to load the original color image
image = cv2.imread("peppers.png")

# Code to convert image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Code to apply Histogram Equalization
equalized_gray = cv2.equalizeHist(gray)

# Code to allow a resize factor for better visualization
resize_factor = 0.5  

# Code to display the original grayscale image
cv2.namedWindow("Original Grayscale", cv2.WINDOW_NORMAL)
cv2.imshow("Original Grayscale", cv2.resize(gray, (0, 0), fx=resize_factor, fy=resize_factor))

# Code to display the Histogram Equalized grayscale image
cv2.namedWindow("Equalized Grayscale", cv2.WINDOW_NORMAL)
cv2.imshow("Equalized Grayscale", cv2.resize(equalized_gray, (0, 0), fx=resize_factor, fy=resize_factor))


# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
