# Machine Vision - Assignment 1
# Author: Christopher Mitchell
# Date: 04/02/25

# ========== Question 2 - Geometric Transformations ========== #

# ========== Part 2: (Define a rotation matrix to rotate the image 45 degrees and then rotate and display the image) ========== #

# Code to import cv2 & numpy
import cv2
import numpy as np

# Code to load the image
image = cv2.imread("Colosseum.JPG")

# Code to get the image dimensions (height, width)
height, width = image.shape[:2]

# Code to define the center of rotation
center = (width // 2, height // 2)

# Code to define the rotation matrix for 45 degrees
angle = 45
scale = 1.0  # Keep scale as 1 to maintain the original size
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Code to actually rotate the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Code to allow resizing of the display window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotated Image (45 degrees)", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotated Full Image (45 degrees)", cv2.WINDOW_NORMAL)

# Code to get the new image dimensions after rotation
cos_val = np.abs(rotation_matrix[0, 0])
sin_val = np.abs(rotation_matrix[0, 1])

# Code to get the new height & width after rotation
new_width = int((height * sin_val) + (width * cos_val))
new_height = int((height * cos_val) + (width * sin_val))

# Code to adjust the rotation matrix for translation
rotation_matrix[0, 2] += (new_width / 2) - center[0]
rotation_matrix[1, 2] += (new_height / 2) - center[1]

# Code to rotate the image with new bounds
rotated_full = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

# Code to display the seperate images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image (45 degrees)", rotated_image)
cv2.imshow("Rotated Full Image (45 degrees)", rotated_full)

# Code to close all windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()


