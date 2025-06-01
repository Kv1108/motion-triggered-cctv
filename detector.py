import cv2
import time
import datetime
import os
from utils import ensure_folder_exists

class MotionDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

        self.detection = False
        self.timer_started = False
        self.detection_stopped_time = None

        self.SECONDS_TO_RECORD_AFTER_DETECTION = 5
        self.video_folder = "recorded_videos"
        ensure_folder_exists(self.video_folder)

        self.frame_size = (int(self.cap.get(3)), int(self.cap.get(4)))
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = None
        self.is_running = True

    def start_detection(self):
        self.is_running = True
        print("[INFO] Detection started")

    def stop_detection(self):
        self.is_running = False
        print("[INFO] Detection stopped")

    def generate(self):
        print("[INFO] Starting video stream...")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            if not self.is_running:
                # Show raw camera feed if not running detection
                ret, jpeg = cv2.imencode('.jpg', frame)
                if not ret:
                    continue
                frame_bytes = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            bodies = self.body_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) + len(bodies) > 0:
                if self.detection:
                    self.timer_started = False
                else:
                    self.detection = True
                    timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    video_path = os.path.join(self.video_folder, f"{timestamp}.mp4")
                    self.out = cv2.VideoWriter(video_path, self.fourcc, 20, self.frame_size)
                    print(f"[INFO] Started recording: {video_path}")
            elif self.detection:
                if self.timer_started:
                    if time.time() - self.detection_stopped_time >= self.SECONDS_TO_RECORD_AFTER_DETECTION:
                        self.detection = False
                        self.timer_started = False
                        if self.out:
                            self.out.release()
                        print("[INFO] Stopped recording")
                else:
                    self.timer_started = True
                    self.detection_stopped_time = time.time()

            if self.detection and self.out:
                self.out.write(frame)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            for (x, y, w, h) in bodies:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            frame_bytes = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    def stop(self):
        self.cap.release()
        if self.out:
            self.out.release()
