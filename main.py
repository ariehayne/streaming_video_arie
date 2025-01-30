import threading

from Streamer import Streamer
from Detector import Detector
from Presenter import Presenter

def main(file_name):
    # Create queues
    frame_queue = []
    detection_queue = []

    # Start system
    streamer = Streamer(file_name, frame_queue)
    detector = Detector(frame_queue, detection_queue, streamer)
    presenter = Presenter(detection_queue, detector)

    streamer_thread = threading.Thread(target=streamer.stream)
    detector_thread = threading.Thread(target=detector.detect_motion)

    streamer_thread.start()
    detector_thread.start()

    # Run presenter on main thread
    presenter.display()

    # Ensure all threads exit properly
    streamer_thread.join()
    detector_thread.join()
    # Use a breakpoint in the code line below to debug your script.
    print(f'finish process for {file_name}')

main('WhatsApp Video 2025-01-13 at 15.56.16_7cacf716.mp4')

