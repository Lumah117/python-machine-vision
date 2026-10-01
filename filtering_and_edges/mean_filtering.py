# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 3 - Smoothing Filters & Edge Detection ========== #

# ========== Part 1: (Apply a mean filter to the image and change kernel size) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the original image
image = cv2.imread("Colosseum.JPG")


# Code to apply Mean Filters with different kernel sizes
kernel_size_5 = cv2.blur(image, (5, 5))  # 5x5 kernel
kernel_size_10 = cv2.blur(image, (10, 10))  # 10x10 kernel
kernel_size_15 = cv2.blur(image, (50, 50))  # 15x15 kernel

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mean Filter (5x5 Kernel)", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mean Filter (10x10 Kernel)", cv2.WINDOW_NORMAL)
cv2.namedWindow("Mean Filter (15x15 Kernel)", cv2.WINDOW_NORMAL)

# Code to display the seperate images
cv2.imshow("Original Image", image)
cv2.imshow("Mean Filter (5x5 Kernel)", kernel_size_5)
cv2.imshow("Mean Filter (10x10 Kernel)", kernel_size_10)
cv2.imshow("Mean Filter (15x15 Kernel)", kernel_size_15)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
