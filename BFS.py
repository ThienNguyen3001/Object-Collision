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