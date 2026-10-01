# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 1 - Image Loading & Conversion ========== #

# ========== Part 2: (Convert the image to greyscale & HSL/HSV) ========== #

# Code to import cv2
import cv2

# Code to load the image
image = cv2.imread("Colosseum.JPG")

# Convert to Grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSL (Hue, Saturation, Lightness)
hsl = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# Convert to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSL Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("HSV Image", cv2.WINDOW_NORMAL)

# Code to display the seperate images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscale)
cv2.imshow("HSL Image", hsl)
cv2.imshow("HSV Image", hsv)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
