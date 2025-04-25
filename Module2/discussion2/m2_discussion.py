# Import necessary libraries
import cv2
import numpy as np
import os # Import os to check if file exists

# --- Configuration ---
# Define the path to the image file - UPDATED with user's path
image_path = 'Module2/discussion2/shutterstock227361781--125.jpg'
translated_output_path = 'Module2/discussion2/img_out/translated_banknotes.jpg'
edges_output_path = 'Module2/discussion2/img_out/edges_banknotes.jpg'
contours_output_path = 'Module2/discussion2/img_out/contours_banknotes.jpg'

# Translation parameters
tx = 70 # Pixels to shift right
ty = 40 # Pixels to shift down

# Canny edge detection parameters
canny_threshold1 = 100 # Lower threshold
canny_threshold2 = 200 # Higher threshold

# --- 1. Import Image and Examine Pixels ---

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: Image file not found at {image_path}")
else:
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    # Check if the image was loaded successfully
    if img is None:
        print(f"Error: Could not load image from {image_path}. Check file format/integrity.")
    else:
        print(f"Image '{image_path}' loaded successfully.")

# Basic Image Examination (only if image loaded correctly)
if img.size > 0: # Check if image is not the placeholder
    print("\n--- Image Pixel Matrix Examination ---")
    print(f"Image shape: {img.shape}") # (height, width, channels) BGR format
    print(f"Data type: {img.dtype}")
    print(f"Total number of pixels: {img.size}")
    if img.shape[0] > 50 and img.shape[1] > 100:
        pixel_value = img[50, 100]
        print(f"Pixel value at (row=50, col=100): {pixel_value} (BGR format)")
    else:
        print("Image dimensions too small to access pixel at (50, 100).")
else:
     print("\nSkipping pixel examination due to image loading error.")


# --- 2. Apply Geometric Transformation (Translation) ---

# Only proceed if the image was loaded correctly
if img.size > 0:
    rows, cols, _ = img.shape # Use _ if channels not needed later

    # Define the translation matrix M
    M = np.float32([
        [1, 0, tx],
        [0, 1, ty]
    ])

    print("\n--- Transformation Details ---")
    print(f"Applying translation: tx = {tx}, ty = {ty}")
    print("Transformation Matrix M:")
    print(M)

    # Apply the affine transformation
    translated_img = cv2.warpAffine(img, M, (cols, rows))

    # Save the translated image
    try:
        cv2.imwrite(translated_output_path, translated_img)
        print(f"\nTranslated image saved successfully as '{translated_output_path}'")
    except Exception as e:
        print(f"\nError saving the translated image: {e}")

else:
    print("\nSkipping translation due to image loading error.")
    translated_img = img # Use the placeholder if translation skipped

# --- 3. Perform Edge Detection ---

# Only proceed if the image was loaded correctly
if img.size > 0:
    print("\n--- Edge Detection ---")
    # Convert the original image to grayscale (edges work best on grayscale)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("Converted original image to grayscale.")

    # Apply Canny edge detection
    edges = cv2.Canny(gray_img, canny_threshold1, canny_threshold2)
    print(f"Applied Canny edge detection with thresholds: {canny_threshold1}, {canny_threshold2}")

    # Save the edge-detected image
    try:
        cv2.imwrite(edges_output_path, edges)
        print(f"Edge detected image saved successfully as '{edges_output_path}'")
    except Exception as e:
        print(f"\nError saving the edge detected image: {e}")
else:
    print("\nSkipping edge detection due to image loading error.")
    # Create placeholder edge map if needed downstream, matching grayscale type
    if img.ndim == 3: # Check if original img was loaded (or is placeholder)
        placeholder_shape = img.shape[:2]
    else: # Handle case where img itself failed to load initially
        placeholder_shape = (300, 400) # Default shape
    edges = np.zeros(placeholder_shape, dtype=np.uint8)


# --- 4. Perform Contour Analysis ---

# Only proceed if the image was loaded correctly and edges were generated
# Check edges shape as it might be a placeholder
if img.size > 0 and edges.size > 0 and np.any(edges): # Check if edges is not all zeros
    print("\n--- Contour Analysis ---")
    # Find contours in the edge map
    # cv2.RETR_EXTERNAL finds only outer contours
    # cv2.CHAIN_APPROX_SIMPLE compresses segments
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Found {len(contours)} external contours.")

    # Create a copy of the original image to draw contours on
    contour_img = img.copy()

    # Draw the contours on the copy image
    # Draw all contours (-1), in green (0, 255, 0), thickness 1
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 1)
    print("Drew contours on a copy of the original image.")

    # Save the image with contours
    try:
        cv2.imwrite(contours_output_path, contour_img)
        print(f"Image with contours saved successfully as '{contours_output_path}'")
    except Exception as e:
        print(f"\nError saving the contour image: {e}")
elif img.size > 0:
     print("\nSkipping contour analysis because no edges were detected.")
     contour_img = img.copy() # Create a copy to avoid errors if display code is uncommented
else:
    print("\nSkipping contour analysis due to image loading error.")
    contour_img = img.copy() # Use placeholder


print("\nScript finished.")

# --- Optional: Display Images (if running locally with a GUI) ---
# Uncomment below if you have a display environment
# if img.size > 0: # Only display if images were processed
#     cv2.imshow('Original Banknotes', img)
#     if 'translated_img' in locals() and translated_img.size > 0:
#        cv2.imshow('Translated Banknotes', translated_img)
#     if 'edges' in locals() and edges.size > 0:
#        cv2.imshow('Edges', edges)
#     if 'contour_img' in locals() and contour_img.size > 0:
#        cv2.imshow('Contours', contour_img)
#     print("\nDisplaying images. Press any key to close the windows.")
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

