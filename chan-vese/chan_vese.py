import cv2
import numpy as np
from skimage.segmentation import chan_vese
from skimage.measure import label

def chan_vese(frame):
    '''
        Hàm chan-vese dùng để segment vùng nền và vùng chứa đối tượng trong ảnh
        Input:
            frame: ảnh cần segment
        Output:
            num_features: số lượng vùng chứa đối tượng
        Để có thể phát hiện đối tượng trong frame, thuật toán sẽ kiểm tra số lượng vùng chứa đối tượng. Tùy vào trường hợp, 
        nếu frame có 2 đối tượng thì num_features = 1 sẽ va chạm, ở trường hợp 3 đối tượng thì num_features = 2 hoặc num_features =1
        sẽ va chạm. 
    '''
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv_result = chan_vese(gray_frame, mu=0.25, lambda1=30, lambda2=30, tol=1e-2, max_num_iter=8, extended_output=True)
    phi = cv_result[1]
    contour_mask = phi > 1
    labeled_contours, num_features = label(contour_mask, return_num=True)
    return num_features