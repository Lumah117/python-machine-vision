# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 4 - Intensity Range Adjustment & Histogram Equalisation ========== #

# ========== Part 3: (Reduce the intensity range of the grayscale image to a lower range and display the image) ========== #

#Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the original color image
image = cv2.imread("peppers.png")

# Code to convert the image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Code for function to reduce intensity range
def reduce_intensity_range(image, N):
    return np.round(image * (N / 255)).astype(np.uint8)

# Code for the different N values to test
N_values = [255, 128, 64, 32, 16, 8]

# Code for more accurate window resizing (adjust this if needed)
resize_factor = 0.5  # Adjust for better display

# Code to display the original color image
cv2.namedWindow("Original Color Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Color Image", cv2.resize(image, (0, 0), fx=resize_factor, fy=resize_factor))

# Code to display the grayscale image
cv2.namedWindow("Grayscale Image", cv2.WINDOW_NORMAL)
cv2.imshow("Grayscale Image", cv2.resize(gray, (0, 0), fx=resize_factor, fy=resize_factor))

# Code to loop through different N values, apply reduction, resize, and display
for N in N_values:
    reduced_image = reduce_intensity_range(gray, N)

    # Code resize the image for display
    resized_image = cv2.resize(reduced_image, (0, 0), fx=resize_factor, fy=resize_factor)

    # Code to create resizable window
    window_name = f"Grayscale with Intensity Range [0, {N}]"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, resized_image)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
