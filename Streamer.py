import cv2

class Streamer:
    def __init__(self, video_path, queue):
        self.video_path = video_path
        self.queue = queue

    def stream(self):
        cap = cv2.VideoCapture(self.video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            self.queue.append((frame, time.time()))
        cap.release()