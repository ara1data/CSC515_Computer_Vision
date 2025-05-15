# Module 4 Critical Thinking Assignment
# Option 1: Mean, Median, and Gaussian Filters 

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# May 11, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# Install matplotlib: pip install matplotlib
# Install required system library for OpenCV: install -qq libgl1
# ------------------------------

# Requirement 0A: Import Appropriate Packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image from root folder
image_path = 'Module4/Mod4CT1.jpg'
image = cv2.imread(image_path)

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kernel sizes and sigma calculation
kernel_sizes = [3, 5, 7]
sigma_pairs = [(0.33, 0.66), (0.66, 1.0), (1.0, 1.5)]  # Two sigmas per kernel

# Create figure with subplots
fig, axs = plt.subplots(3, 4, figsize=(18, 12))

# Column titles
col_titles = ['Mean Filter', 'Median Filter', 'Gaussian σ1', 'Gaussian σ2']

# Process each kernel size
for row, k in enumerate(kernel_sizes):
    # Apply filters
    mean = cv2.blur(image_rgb, (k, k))
    median = cv2.medianBlur(image_rgb, k)
    gauss1 = cv2.GaussianBlur(image_rgb, (k, k), sigma_pairs[row][0])
    gauss2 = cv2.GaussianBlur(image_rgb, (k, k), sigma_pairs[row][1])

    # Display results
    axs[row, 0].imshow(mean)
    axs[row, 1].imshow(median)
    axs[row, 2].imshow(gauss1)
    axs[row, 3].imshow(gauss2)
    
    # Set labels
    axs[0, 0].set_title(col_titles[0], fontsize=10)
    axs[0, 1].set_title(col_titles[1], fontsize=10)
    axs[0, 2].set_title(f'{col_titles[2]} ({sigma_pairs[row][0]})', fontsize=10)
    axs[0, 3].set_title(f'{col_titles[3]} ({sigma_pairs[row][1]})', fontsize=10)
    axs[row, 0].set_ylabel(f'{k}x{k} Kernel', fontsize=10)

    # Remove ticks
    for col in range(4):
        axs[row, col].set_xticks([])
        axs[row, col].set_yticks([])

plt.tight_layout()
plt.savefig('filter_comparison.jpg', dpi=300)
plt.show()
