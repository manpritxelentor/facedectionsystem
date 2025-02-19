import cv2
import time
import face_recognition
from face_detector import detect_faces

def motion_trigger():
    """Trigger face detection when motion is detected."""
    while True:
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
        video_capture.release()

        if not ret:
            continue

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:  
            video_capture = cv2.VideoCapture(0)
            detect_faces(video_capture)  

        time.sleep(1)  

if __name__ == "__main__":
    motion_trigger()
