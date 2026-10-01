# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 4 - Intensity Range Adjustment & Histogram Equalisation ========== #

# ========== Part 1: (Load and display the image, examine and report image details (width, height, etc.)) ========== #

# Code to import cv2
import cv2

# Code to load the 'peppers.png' image 
image = cv2.imread("peppers.png")  

# Code to get image dimensions
height, width, channels = image.shape  # shape returns (height, width, channels)

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)

# Code to display the image
cv2.imshow("Original Image", image)

# Code to print all the image details
print(f"Image Dimensions:")
print(f"Width: {width} pixels")
print(f"Height: {height} pixels")
print(f"Number of Channels: {channels} (3 for RGB, 4 for RGBA if transparency exists)")

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
