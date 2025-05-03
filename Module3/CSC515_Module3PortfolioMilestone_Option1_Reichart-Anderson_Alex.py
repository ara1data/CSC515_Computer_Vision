# Module 3 Portfolio Milestone 2
# Option 1: Drawing Functions in OpenCV

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# May 4, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# ------------------------------

# Requirement 0A: Import Appropriate Packages
import cv2
import os

# Requirement 0B: Load the pre-trained Haar cascade classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Requirement 1: Load Image of My Face
image_path = 'Module3/image_of_alex.jpg'  # Image Path from Module 3 (root) Folder
image = cv2.imread(image_path)

# Convert image to grayscale for detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect face in the image
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Process each detected face
for (x, y, w, h) in face:
    # Calculate the center and radius for the circle around the face
    center = (x + w // 2, y + h // 2)
    radius = int(max(w, h) / 2)
    # Draw a green circle around the face (color in BGR format: (0, 255, 0))
    cv2.circle(image, center, radius, (0, 255, 0), 2)
    
    # Define the region of interest (ROI) for eyes within the face
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    
    # Detect eyes within the face ROI
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3)
    for (ex, ey, ew, eh) in eyes:
        # Draw a red rectangle around each eye (color in BGR format: (0, 0, 255))
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)

# Add text "this is me" to the image
cv2.putText(image, "this is me", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the annotated image
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)  # Wait for any key press to close the window

# Requirement 3: Write Python code to write a copy of the image to any directory on your desktop.
output_dir = './Module3/image_output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'drawn_on_image.jpg')
cv2.imwrite(output_path, image)
print(f"Image successfully saved to: {output_path}")

# Close all windows
cv2.destroyAllWindows()
