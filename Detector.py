import numpy as np
from skimage import color


class Detector:
    def __init__(self, queue, output_queue, streamer):
        self.queue = queue
        self.output_queue = output_queue
        self.streamer = streamer
        self.running = True

    def detect_motion(self):
        prev_frame = None
        while self.running:
            if self.queue:
                # I added this part to improve performance,
                # It's easier to go with one image (gray) than with 3 images (RGB)
                frame, timestamp = self.queue.pop(0)
                gray = color.rgb2gray(frame)

                if prev_frame is None:
                    prev_frame = gray
                    continue

                motion_mask = np.abs(gray - prev_frame) > 0.1
                prev_frame = gray

                self.output_queue.append((frame, motion_mask, timestamp))
            elif not self.streamer.running:
                self.running = False
        print('Detector is done')
        self.output_queue.append((None, None, None))