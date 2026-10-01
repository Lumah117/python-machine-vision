# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 2 - Geometric Transformations ========== #

# ========== Part 1: (Perform a Translation on the image using a matrix and display the translated image) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the original image
image = cv2.imread("Colosseum.JPG")

# Code to get image dimensions (height, width)
height, width = image.shape[:2]

# Code to define the translation matrix
tx, ty = 50, 30  # Shift by 50 pixels right and 30 pixels down
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

# Code to apply the translation
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Translated Image", cv2.WINDOW_NORMAL)

# Code to display the original and translated images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
