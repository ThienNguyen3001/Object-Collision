import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import active_contour
from skimage.filters import threshold_otsu
from pytictoc import TicToc

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def calculate_centroid(contour):
    moments = cv2.moments(contour)
    if moments["m00"] != 0:
        cx = int(moments["m10"] / moments["m00"])
        cy = int(moments["m01"] / moments["m00"])
        return (cx, cy)
    return None

def detect_collision(centroid1, centroid2, threshold_distance):
    """Kiểm tra va chạm giữa hai đối tượng dựa trên khoảng cách giữa các centroid."""
    if centroid1 and centroid2:
        # Tính khoảng cách giữa hai centroid
        distance = calculate_distance(centroid1, centroid2)
        if distance <= threshold_distance:
            return True
    return False 