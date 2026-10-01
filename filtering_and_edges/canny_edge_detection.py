# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 3 - Smoothing Filters & Edge Detection ========== #

# ========== Part 3: (Apply a canny edge detector to a grayscale image and experiment with different threshold values) ========== #

# Code to import cv2 
import cv2

# Code to load the original image
image = cv2.imread("Colosseum.JPG")

# Code to convert image to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Code to apply Canny Edge Detector with different threshold values
canny_low = cv2.Canny(gray, 50, 100)   # Lower thresholds
canny_medium = cv2.Canny(gray, 100, 200) # Medium thresholds
canny_high = cv2.Canny(gray, 150, 250)  # Higher thresholds

# Code to allow resizing of the display window
cv2.namedWindow("Original Grayscale", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edges (50,100)", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edges (100,200)", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny Edges (150,250)", cv2.WINDOW_NORMAL)

# Code to display the seperate images
cv2.imshow("Original Grayscale", gray)
cv2.imshow("Canny Edges (50,100)", canny_low)
cv2.imshow("Canny Edges (100,200)", canny_medium)
cv2.imshow("Canny Edges (150,250)", canny_high)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
