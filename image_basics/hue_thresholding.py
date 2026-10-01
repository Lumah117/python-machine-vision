# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 1 - Image Loading & Conversion ========== #

# ========== Part 3b: (Binarise the greyscale image using a threshold based on hue and display the binarised image) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the image
image = cv2.imread("Colosseum.JPG")


# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Extract the Hue channel (H is the first channel in HSV)
hue_channel = hsv[:, :, 0]

# Code to apply a binary threshold on the Hue channel
hue_threshold = 120  # Adjust this value based on your desired color separation
_, hue_binary = cv2.threshold(hue_channel, hue_threshold, 255, cv2.THRESH_BINARY)

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Hue Channel Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Hue Binarised Image", cv2.WINDOW_NORMAL)

# Code to display the original and binarized images
cv2.imshow("Original Image", image)
cv2.imshow("Hue Channel Image", hue_channel)
cv2.imshow("Hue Binarised Image", hue_binary)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
