import cv2
import time

class Streamer:
    def __init__(self, video_path, queue):
        self.video_path = video_path
        self.queue = queue
        self.running = True

    def stream(self):
        cap = cv2.VideoCapture(self.video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert OpenCV BGR to RGB format
            self.queue.append((frame, time.time()))
        cap.release()
        self.running = False