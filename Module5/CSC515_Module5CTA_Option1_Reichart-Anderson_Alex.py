# Module 5 Critical Thinking Assignment
# Option 1: Morphology Operations for Fingerprint Enhancement 

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# May 18, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# Install matplotlib: pip install matplotlib
# Install required system library for OpenCV: install -qq libgl1
# ------------------------------

# Requirement 0A: Import Appropriate Packages

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the latent fingerprint image and convert to grayscale
image_path = 'Module5/Module5CTA_fingerprint.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel) of size 3x3
kernel = np.ones((3, 3), np.uint8)

# Apply morphological operations
erosion = cv2.erode(image, kernel, iterations=1) # Erosion
dilation = cv2.dilate(image, kernel, iterations=1) # Dialation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) # Opening
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) # Closing

# Display the results using matplotlib for visualization
titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing']
images = [image, erosion, dilation, opening, closing]

plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.tight_layout()
plt.show()
