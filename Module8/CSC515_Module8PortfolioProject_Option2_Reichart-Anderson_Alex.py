# Module 8 Portfolio Project
# Option 2: Face Detection and Privacy 

# Alexander Reichart-Anderson
# MS in AI and ML, Colorado State University Global
# CSC515-1: Foundations of Computer Vision
# Dr. Jack Li
# June 8, 2025

# ------------------------------
# To Install OpenCV: pip3 install opencv-python
# Install required system library for OpenCV: install -qq libgl1
# ------------------------------

# Requirement 0A: Import Appropriate Packages

import cv2
import numpy as np

# Requirement 1: Load Classifiers

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Requirement 2: Face and Eye Detection with Anonymization
def detect_and_blur_eyes(image_path):
    
    # 2A: Load Images
    img = cv2.imread(image_path)
    if img is None:
        return None, 'Image not found or unable to load'
    
    # 2B: Convert to grayscale for detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2C: Detect faces with optimized parameters
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # 2D: For Loop for Drawing and Blurring
    for (x, y, w, h) in faces:
        # 2E: Draw red bounding box around face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
        # 2F: Process face region
        face_roi_gray = gray[y:y+h, x:x+w]
        face_roi_color = img[y:y+h, x:x+w]
        
        # 2G: Detect eyes with alignment consideration
        eyes = eye_cascade.detectMultiScale(
            face_roi_gray,
            scaleFactor=1.05,
            minNeighbors=3
        )
        
        # 2H: Blur detected eyes
        for (ex, ey, ew, eh) in eyes:
            eye_region = face_roi_color[ey:ey+eh, ex:ex+ew]
            blurred_eye = cv2.GaussianBlur(eye_region, (99, 99), 30)
            face_roi_color[ey:ey+eh, ex:ex+ew] = blurred_eye
    
    return img, None

# Requirement 3: Function Call for three images
# 3A: Load Images
images = ['Module8/images_original/group_photo.jpg', 'Module8/images_original/blurry_group.jpg', 'Module8/images_original/person_with_dog.jpg']
# 3B: Function Calling
for idx, img_path in enumerate(images):
    result, error = detect_and_blur_eyes(img_path)
    if error is None:
        cv2.imwrite(f'output_{idx+1}.jpg', result)
    else:
        print(f"Error processing {img_path}: {error}")
