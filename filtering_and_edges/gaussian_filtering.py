# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 3 - Smoothing Filters & Edge Detection ========== #

# ========== Part 2: (Apply a gaussian filter to the image & experiment with different deviations) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the original image
image = cv2.imread("Colosseum.JPG")

# C for function to dynamically determine the kernel size based on σ
def get_dynamic_kernel_size(sigma):
    return int(6 * sigma + 1)  # Ensure kernel size is an odd number

# Code to define sigma values
sigma_values = [10, 20, 40]

# Code for dictionary to store blurred images
blurred_images = {}

# Code to apply Gaussian Blur dynamically
for sigma in sigma_values:
    kernel_size = get_dynamic_kernel_size(sigma)  # Compute kernel size
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    blurred_images[sigma] = blurred  # Store the blurred image

    # Code to create a resizable window for each blurred image
    cv2.namedWindow(f"Gaussian Blur (Sigma={sigma}, Kernel={kernel_size}x{kernel_size})", cv2.WINDOW_NORMAL)
    cv2.imshow(f"Gaussian Blur (Sigma={sigma}, Kernel={kernel_size}x{kernel_size})", blurred)

# Code to allow resizing of the display window for the original image
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", image)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
