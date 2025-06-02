# Module 6 Critical Thinking Assignment
# Option 1: Adaptive Thresholding Scheme for Simple Objects 

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# May 25, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# Install matplotlib: pip install matplotlib
# Install required system library for OpenCV: install -qq libgl1
# ------------------------------

# Requirement 0A: Import Appropriate Packages

import cv2
import os

# Function to apply adaptive thresholding and save/display results
def apply_adaptive_thresholding(image_path, output_folder, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, block_size=21, C=10):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(img, 255, method, cv2.THRESH_BINARY_INV, block_size, C)
    
    # Create output filename
    base_name = os.path.basename(image_path).split('.')[0]
    output_path = os.path.join(output_folder, f"{base_name}_thresholded.png")
    
    # Save the thresholded image
    cv2.imwrite(output_path, thresh)
    print(f"Processed and saved: {output_path}")
    
    # Display original and thresholded images (optional, comment out if not needed)
    cv2.imshow("Original Image", img)
    cv2.imshow("Thresholded Image", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main execution
if __name__ == "__main__":
    # Define paths to the three images (replace with actual paths)
    image_paths = {
        "indoor": "Module6/images_org/indoor_image.jpg",
        "outdoor": "Module6/images_org/outdoor_image.jpg",
        "closeup": "Module6/images_org/closeup_image.jpg"
    }
    
    # Define output folder
    output_folder = "thresholded_results"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each image with adaptive thresholding
    for scene_type, path in image_paths.items():
        print(f"Processing {scene_type} scene...")
        # You can adjust block_size and C for different images if needed
        apply_adaptive_thresholding(path, output_folder, method=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, block_size=21, C=10)