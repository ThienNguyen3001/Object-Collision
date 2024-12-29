import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

from collections import deque

def bfs(img,visited,i,j):
    queue = deque([(i,j)])
    visited[i][j] = True
    pixel = []

    while queue:
        x, y = queue.popleft()
        pixel.append((x,y))
        for nx in range(x - 1, x + 2):  
            for ny in range(y - 1, y + 2): 
                if 0 <= nx < len(img) and 0 <= ny < len(img[0]):
                    if not visited[nx][ny] and img[nx,ny] == 0:
                        visited[nx][ny] = True
                        queue.append((nx, ny)) 
    return pixel                       

def all_components(img):
    rows, cols = img.shape
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and img[i,j] == 0:
                bfs(img,visited,i,j)
                components+=1

    return components

def objCollision(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Không thể mở video.")
        exit()

    while True:
        ret, frame = cap.read()
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

        if not ret:
            break
        
        grad_magnitude = cv2.Canny(frame,100,200)
        if all_components(frame) == 1:
            print(f"Chạm nhau tại: {current_time_ms}")
            break
    
    print("không chạm nhau")
        
        
def bfs(img,visited,i,j):
    queue = deque([(i,j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for nx in range(x - 1, x + 2):  
            for ny in range(y - 1, y + 2): 
                if 0 <= nx < len(img) and 0 <= ny < len(img[0]):
                    if not visited[nx][ny] and img[x,y] == img[nx,ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))                 

def all_components(img):
    rows, cols = img.shape
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    components = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                bfs(img,visited,i,j)
                components+=1

    return components

def objCollision(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Không thể mở video.")
        exit()
    frame_count = 0
    pastComponents = 0
    while True:
        ret, frame = cap.read()
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

        if not ret:
            print("không chạm nhau")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_frame, (5, 5), 0)
        _, binary = cv2.threshold(blurred, 147, 255, cv2.THRESH_BINARY_INV)

        currentComponents = all_components(binary)
        if pastComponents > currentComponents:
            print(f"Chạm nhau tại: {current_time_ms}, Frame: {frame_count}")
            break
        pastComponents = currentComponents
        frame_count+=1