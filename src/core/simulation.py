import cv2
import numpy as np
import math
import random
from datetime import datetime
import os

class Ball:
    def __init__(self, x, y, dx, dy, radius, color, WIDTH, HEIGHT):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

    def move(self):
        if self.x - self.radius < 0 or self.x + self.radius > self.WIDTH:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.HEIGHT:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy

    def draw(self, frame):
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, self.color, -1)

# Tạo danh sách ngẫu nhiên các quả bóng
def create_balls(n, WIDTH, HEIGHT,ColorBall):
    balls = []
    for _ in range(n):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        dx = 5
        dy = 5
        radius = random.randint(25, 35)
        if ColorBall == None:
            color = tuple(random.randint(0, 255) for _ in range(3))  
        else:
            color = ColorBall
        balls.append(Ball(x, y, dx, dy, radius, color, WIDTH, HEIGHT))
    return balls

def check_collision(ball1, ball2):
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx * dx + dy * dy)
    if distance < ball1.radius + ball2.radius:
        angle = math.atan2(dy, dx)
        sin = math.sin(angle)
        cos = math.cos(angle)

        temp_dx = ball1.dx
        temp_dy = ball1.dy
        ball1.dx = ball2.dx
        ball1.dy = ball2.dy
        ball2.dx = temp_dx
        ball2.dy = temp_dy

        overlap = (ball1.radius + ball2.radius - distance) / 2
        ball1.x -= overlap * cos
        ball1.y -= overlap * sin
        ball2.x += overlap * cos
        ball2.y += overlap * sin

def Simulation_Methods(n, background = (255,255,255), DURATION = 3, WIDTH = 600, HEIGHT = 400, ColorBall = None):
    # Thiết lập thông số video
    FPS = 30
    FRAMES = DURATION * FPS

    # Kiểm tra thư mục
    video_folder = os.path.join("data", "video")
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    # Khởi tạo video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = os.path.join(video_folder, f'ball_simulation_{timestamp}.mp4')
    out = cv2.VideoWriter(video_path, fourcc, FPS, (WIDTH, HEIGHT))

    # Khởi tạo n quả bóng ngẫu nhiên
    balls = create_balls(n,WIDTH,HEIGHT,ColorBall)

    # Tạo các khung hình
    for frame_index in range(FRAMES):
        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        frame[:] = background

        for ball in balls:
            ball.move()
            ball.draw(frame)

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                check_collision(balls[i], balls[j])

        out.write(frame)

    out.release()
    print(f"Video saved as ball_simulation_{timestamp}.mp4")
