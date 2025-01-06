import cv2
import numpy as np
import matplotlib.pyplot as plt
from pytictoc import TicToc
from skimage.segmentation import active_contour

def calculate_area(contour):
    return cv2.contourArea(contour)

def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 147, 255, cv2.THRESH_BINARY)
    contours, hierachy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
    
    max_area = 0.5 * frame.shape[0] * frame.shape[1]
    filtered_contours = [contour for contour in contours if cv2.contourArea(contour) < max_area]

    return filtered_contours

def detect_collision_by_area(contours, previous_total_area, threshold=100):
    total_area = sum(calculate_area(contour) for contour in contours)
    if abs(total_area - previous_total_area) > threshold:
        return True, total_area
    return False, total_area

def check_collision_active_contour_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    frame_number = 0
    t = TicToc()
    t.tic()

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    previous_total_area = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #contours = preprocess_frame(frame)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ret, binary = cv2.threshold(gray, 147, 255, cv2.THRESH_BINARY)
        # contours, hierachy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # collision_detected, current_total_area = detect_collision_by_area(contours, previous_total_area)

        # # Loại bỏ các contour có diện tích lớn hơn ngưỡng
        # max_area = 0.5 * frame.shape[0] * frame.shape[1]
        # filtered_contours = [contour for contour in contours if cv2.contourArea(contour) < max_area]
        
        # result_img = frame.copy()
        # for contour in filtered_contours:  # Chỉ vẽ contour đã lọc
        #     cv2.drawContours(result_img, [contour], -1, (0, 255, 0), 10)
        filtered_contours = preprocess_frame(frame)
        collision_detected, current_total_area = detect_collision_by_area(filtered_contours, previous_total_area)

        result_img = frame.copy()
        for contour in filtered_contours:
            cv2.drawContours(result_img, [contour], -1, (0, 255, 0), 10)

        # result_img = frame.copy()
        # for contour in contours:
        #     cv2.drawContours(result_img, [contour], -1, (0, 255, 0), 2)

        status_text = "Collision Detected!" if collision_detected else "No Collision"
        cv2.putText(result_img, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255) if collision_detected else (0, 255, 0), 2)
        cv2.putText(result_img, f"Frame: {frame_number}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        out.write(result_img)

        if collision_detected:
            collision_time = frame_number / fps
            print(f"Collision detected at frame {frame_number} ({collision_time:.2f} seconds)")

        previous_total_area = current_total_area
        frame_number += 1

    cap.release()
    out.release()
    t.toc()
    print(f"Processed {frame_number} frames. Output saved to {output_path}.")