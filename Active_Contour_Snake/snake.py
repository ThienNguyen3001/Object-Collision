import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import active_contour
from skimage.filters import gaussian
def is_connected_with_snake(image, snake):
    rows, cols = image.shape

    # Tạo mặt nạ (mask) từ đường viền của snake
    mask = np.zeros((rows, cols), dtype=np.uint8)
    snake_points = np.round(snake).astype(int)  # Làm tròn tọa độ snake
    cv2.fillPoly(mask, [snake_points], 1)  # Điền vùng bên trong snake với giá trị 1

    dsu = DSU(rows * cols)

    # Duyệt qua các pixel trong mặt nạ
    for r in range(rows):
        for c in range(cols):
            if mask[r, c] == 1:  # Pixel thuộc đối tượng (bên trong snake)
                # Liên kết với các pixel lân cận
                for dr, dc in [(0, 1), (1, 0)]:  # Phải, dưới
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and mask[nr, nc] == 1:
                        dsu.union(r * cols + c, nr * cols + nc)

    # Kiểm tra có duy nhất một tập chứa tất cả pixel bên trong snake
    snake_pixels = [r * cols + c for r in range(rows) for c in range(cols) if mask[r, c] == 1]
    if not snake_pixels:
        return False

    root = dsu.find(snake_pixels[0])
    return all(dsu.find(pixel) == root for pixel in snake_pixels)