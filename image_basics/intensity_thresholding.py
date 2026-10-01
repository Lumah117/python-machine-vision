# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 1 - Image Loading & Conversion ========== #

# ========== Part 3a: (Binarise the greyscale image using a threshold based on intensity and display the binarised image) ========== #

#Code to import cv2
import cv2

# Code to load the image
image = cv2.imread("Colosseum.JPG")

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Code to apply an appropriate binary threshold
threshold_value = 90 # Adjust between 0-255
_, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Code to allow resizing of the display window
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binarised Image", cv2.WINDOW_NORMAL)

# Code to display the seperate images
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Binarised Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
