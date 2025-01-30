import cv2
import time
import numpy as np
class Presenter:
    def __init__(self, queue, detector):
        self.queue = queue
        self.detector = detector

    def display(self):
        cv2.startWindowThread()
        while self.detector.running or self.queue:
            if self.queue:
                frame, motion_mask, timestamp = self.queue.pop(0)

                if frame is None:  # Stop when end signal is received
                    break

                time_str = time.strftime('%H:%M:%S', time.gmtime(timestamp))

                # Convert to BGR for OpenCV display
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # Ensure the frame format is valid
                if frame_bgr is None or motion_mask is None:
                    continue

                # Display frame with time overlay
                cv2.putText(frame_bgr, time_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Video", frame_bgr)
                cv2.imshow("Motion Mask", (motion_mask * 255).astype(np.uint8))

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                cv2.destroyAllWindows()
                for i in range(1, 5):
                    cv2.waitKey(1)