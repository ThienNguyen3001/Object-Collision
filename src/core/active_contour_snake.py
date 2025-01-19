import cv2
import numpy as np
from skimage.filters import gaussian
from skimage.segmentation import active_contour

def active_contour_snake(image, centroids, radii):
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

def collision_snake(snakes, threshold):
    collisions = []
    for i in range(len(snakes)):
        for j in range(i + 1, len(snakes)):
            min_distance = np.inf  #dist tối thiểu
            for point_i in snakes[i]:
                for point_j in snakes[j]:
                    dist = np.linalg.norm(point_i - point_j)
                    if dist < min_distance:
                        min_distance = dist
                        
            if min_distance < threshold:
                # collisions.append((i, j))
                return True
    return False
    
    