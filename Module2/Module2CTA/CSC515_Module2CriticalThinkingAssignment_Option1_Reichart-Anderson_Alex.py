# Import necessary packages
import numpy as np
import cv2
import os

# 2D Puppy Image Path
image_path = "Module2/Module2CTA/shutterstock215592034--250.jpg" 

try:
    # Load puppy image
    image = cv2.imread(image_path)
    
    # Error handling is path is broken
    if image is None:
        raise Exception("Failed to load the image. Check the file path.")
    
    # Display original image
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    
    # Split the image into blue, green, and red channels
    (B, G, R) = cv2.split(image)
    
    # Display each channel individually as grayscale images
    cv2.imshow("Blue Channel", B)
    cv2.imshow("Green Channel", G)
    cv2.imshow("Red Channel", R)
    cv2.waitKey(0)
    
    # Merge the channels back to form the original image
    merged_original = cv2.merge([B, G, R])
    cv2.imshow("Merged Original Image", merged_original)
    cv2.waitKey(0)
    
    # Swap Red and Green channels to create a GRB image (Blue, Red, Green order)
    swapped_channels = cv2.merge([B, R, G])
    cv2.imshow("Swapped Channels (GRB)", swapped_channels)
    cv2.waitKey(0)

    # Save swapped_channels (3D) image
    output_dir = './Module2/Module2CTA/image_output'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, '3d_puppy.jpg')
    cv2.imwrite(output_path, swapped_channels)
    print(f"Image successfully saved to: {output_path}")
    
# Error handling and end of the code
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close all OpenCV windows
    cv2.destroyAllWindows()
