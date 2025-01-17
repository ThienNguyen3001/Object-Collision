import cv2
import numpy as np
from skimage.filters import gaussian
from skimage.segmentation import active_contour

def process_frame_watershed(frame):
    """
    Xử lý frame và trả về markers, tọa độ markers và bán kính
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Ngưỡng để phân tách đối tượng
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    # Áp dụng morphology để tách các đối tượng chạm nhau
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Background rõ ràng
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    
    # Foreground rõ ràng
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.4 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    
    # Vùng không chắc chắn
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Gán nhãn cho vùng foreground
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    
    # Áp dụng watershed
    markers = cv2.watershed(frame, markers)
    
    # Lấy unique markers (bỏ qua background (-1) và unknown (0))
    unique_markers = np.unique(markers)[2:]
    
    centroids = []
    radii = []
    
    for marker in unique_markers:
        mask = np.uint8(markers == marker)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        M = cv2.moments(contours[0])
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            centroids.append((cx, cy))
            
            # Tính bán kính gần đúng từ contour
            radius = np.sqrt(cv2.contourArea(contours[0]) / np.pi)
            radii.append(radius)
    
    return centroids, radii

def apply_active_contour(image, centroids, radii):
    """Tạo snakes từ dữ liệu centroid và bán kính"""
    snakes = []
    s = np.linspace(0, 2 * np.pi, 400)
    for (cx, cy), radius in zip(centroids, radii):
        init_snake = np.array([cy + radius * np.sin(s), cx + radius * np.cos(s)]).T
        snake = active_contour(
            image,
            init_snake,
            alpha=0.015,
            beta=0.1,
            gamma=0.001,
            w_line=0,
            w_edge=1,
            max_px_move=1.0,
            max_num_iter=2500,
            convergence=0.1,
            boundary_condition='periodic'
        )
        snakes.append(snake)
    return snakes