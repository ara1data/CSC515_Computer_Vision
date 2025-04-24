# pip install opencv-python numpy

# Import necessary libraries
import cv2
import numpy as np
import os 

# --- 1. Import Image and Examine Pixels ---

# Load image
image_path = 'shutterstock227361781--125.jpg'
output_image_path = 'transformed_banknotes.jpg'

# Error handling: check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
else:
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Error handling: check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from {image_path}.")
    else:
        print(f"Image '{image_path}' loaded successfully.")

# Examine the pixel matrix (NumPy array)
print("\n--- Image Pixel Matrix Examination ---")
print(f"Image shape: {image.shape}") # BGR format
print(f"Data type: {image.dtype}")
print(f"Total number of pixels: {image.size}")

# Accessing a specific pixel (e.g., at row 50, column 100)
# OpenCV uses (y, x) coordinates, where y is row, x is column
if image.shape[0] > 50 and image.shape[1] > 100:
    pixel_value = image[50, 100]
    print(f"Pixel value at (row=50, col=100): {pixel_value} (BGR format)")
else:
    print("Image dimensions are too small to access pixel at (50, 100).")

# --- 2, 3, 4. Define and Apply Translation (as discussed) ---

# Get image dimensions
rows, cols, channels = image.shape

# Define the translation matrix M
# Translation to 70 pixels to the right (tx=70) and 40 pixels down (ty=40)
tx = 70
ty = 40
# The transformation matrix (M) is a 2x3 NumPy array
M = np.float32([
    [1, 0, tx],  
    [0, 1, ty]   
])

# Print translation matrix
print("\n--- Transformation Details ---")
print(f"Applying translation: tx = {tx}, ty = {ty}")
print("Transformation Matrix M:")
print(M)

# Apply the affine transformation (translation)
# cv2.warpAffine(source_image, transformation_matrix, output_image_size)
# Output image size is specified as (width, height) which is (cols, rows)
translated_img = cv2.warpAffine(image, M, (cols, rows))

# --- 5. Save the Transformed Image ---

# Save the resulting image to a file
try:
    cv2.imwrite(output_image_path, translated_img)
    print(f"\nTransformed image saved successfully as '{output_image_path}'")
except Exception as e:
    print(f"\nError saving the transformed image: {e}")