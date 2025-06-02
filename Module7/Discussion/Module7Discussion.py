import cv2
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

# Create synthetic image
img = np.full((200, 200), 50, dtype=np.uint8)  # Background intensity 50
cv2.rectangle(img, (50, 50), (100, 100), 200, thickness=-1)  # Filled square with intensity 200
cv2.circle(img, (150, 150), 30, 150, thickness=-1)  # Filled circle with intensity 150

# Create ground truth edge map
gt_edges = np.zeros_like(img)
gt_edges[50:101, 50] = 255  # Left edge of square
gt_edges[50:101, 100] = 255  # Right edge of square
gt_edges[50, 50:101] = 255  # Top edge of square
gt_edges[100, 50:101] = 255  # Bottom edge of square

# Circle edges using cv2.circle with thickness 1
cv2.circle(gt_edges, (150, 150), 30, 255, thickness=1)

# Edge detection functions
def detect_edges_canny(image, low_thresh, high_thresh):
    return cv2.Canny(image, low_thresh, high_thresh)

def detect_edges_sobel(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    sobel = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    _, sobel_binary = cv2.threshold(sobel, 50, 255, cv2.THRESH_BINARY)
    return sobel_binary

def detect_edges_laplacian(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    abs_laplacian = cv2.convertScaleAbs(laplacian)
    _, laplacian_binary = cv2.threshold(abs_laplacian, 50, 255, cv2.THRESH_BINARY)
    return laplacian_binary

# Evaluation function
def evaluate_edges(detected, ground_truth):
    detected_bin = (detected > 0).astype(int).flatten()
    gt_bin = (ground_truth > 0).astype(int).flatten()
    precision = precision_score(gt_bin, detected_bin)
    recall = recall_score(gt_bin, detected_bin)
    f1 = f1_score(gt_bin, detected_bin)
    return precision, recall, f1

# Detect edges on original image
canny_edges = detect_edges_canny(img, 100, 200)
sobel_edges = detect_edges_sobel(img)
laplacian_edges = detect_edges_laplacian(img)

# Evaluate on original image
canny_eval = evaluate_edges(canny_edges, gt_edges)
sobel_eval = evaluate_edges(sobel_edges, gt_edges)
laplacian_eval = evaluate_edges(laplacian_edges, gt_edges)

# Add Gaussian noise
noise = np.random.normal(0, 25, img.shape).astype(np.int16)
noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

# Change intensities
noisy_img[50:101, 50:101] = np.clip(noisy_img[50:101, 50:101] + 30, 0, 255)  # Increase square intensity
noisy_img = noisy_img.copy()
noisy_img = noisy_img.astype(np.uint8)
cv2.circle(noisy_img, (150, 150), 30, 100, thickness=-1)  # Change circle intensity to 100

# Detect edges on noisy image with adjusted thresholds
canny_edges_noisy = detect_edges_canny(noisy_img, 50, 150)
sobel_edges_noisy = detect_edges_sobel(noisy_img)
laplacian_edges_noisy = detect_edges_laplacian(noisy_img)

# Evaluate on noisy image
canny_eval_noisy = evaluate_edges(canny_edges_noisy, gt_edges)
sobel_eval_noisy = evaluate_edges(sobel_edges_noisy, gt_edges)
laplacian_eval_noisy = evaluate_edges(laplacian_edges_noisy, gt_edges)

# Print evaluation results
print("Original Image Evaluation:")
print(f"Canny: Precision={canny_eval[0]:.3f}, Recall={canny_eval[1]:.3f}, F1={canny_eval[2]:.3f}")
print(f"Sobel: Precision={sobel_eval[0]:.3f}, Recall={sobel_eval[1]:.3f}, F1={sobel_eval[2]:.3f}")
print(f"Laplacian: Precision={laplacian_eval[0]:.3f}, Recall={laplacian_eval[1]:.3f}, F1={laplacian_eval[2]:.3f}")

print("\nNoisy Image Evaluation:")
print(f"Canny: Precision={canny_eval_noisy[0]:.3f}, Recall={canny_eval_noisy[1]:.3f}, F1={canny_eval_noisy[2]:.3f}")
print(f"Sobel: Precision={sobel_eval_noisy[0]:.3f}, Recall={sobel_eval_noisy[1]:.3f}, F1={sobel_eval_noisy[2]:.3f}")
print(f"Laplacian: Precision={laplacian_eval_noisy[0]:.3f}, Recall={laplacian_eval_noisy[1]:.3f}, F1={laplacian_eval_noisy[2]:.3f}")

# Create a grid image to display all images
# Convert all images to 3-channel for visualization
images = [img, gt_edges, canny_edges, sobel_edges, laplacian_edges, noisy_img, canny_edges_noisy, sobel_edges_noisy, laplacian_edges_noisy]
images_color = [cv2.cvtColor(im, cv2.COLOR_GRAY2BGR) for im in images]

# Create a 3x3 grid
row1 = np.hstack(images_color[0:3])  # Original, Ground Truth, Canny
row2 = np.hstack(images_color[3:6])  # Sobel, Laplacian, Noisy
row3 = np.hstack(images_color[6:9])  # Canny Noisy, Sobel Noisy, Laplacian Noisy
grid_image = np.vstack([row1, row2, row3])

# Save the grid image
cv2.imwrite('edge_detection_grid.png', grid_image)

# Optional: Print grid image shape as confirmation
print("\nGrid Image Shape:", grid_image.shape)