# Module 1 Portfolio Milestone 1
# Option 2: Installing OpenCV

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# April 20, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# ------------------------------

# Requirement 0: Import Appropriate Packages
import cv2
import os

# Requirement 1: Write Python code to import the following image: numbers image.Download numbers image.
image_path = 'Module1/shutterstock130285649--250.jpg'  # Image Path from Module 1 (root) Folder
image = cv2.imread(image_path)

# Error handling if the image is not loaded in requirement 1
if image is None:
    print("Image not found. Please check the path and filename.")
else:

# Requirement 2: Write Python code to display the image.
    cv2.imshow('Numbers Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Requirement 3: Write Python code to write a copy of the image to any directory on your desktop.
    output_dir = './Module1/image_output'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'numbers_image_copy.jpg')
    cv2.imwrite(output_path, image)
    print(f"Image successfully saved to: {output_path}")

# Alternate Requirement # 3 Implementation for the Desktop

"""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop_path, 'numbers_image_copy.jpg')
    cv2.imwrite(output_path, image)
    print(f"Image successfully saved to: {output_path}")
"""
