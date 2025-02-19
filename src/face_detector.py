import cv2
import numpy as np
import face_recognition
import csv
from datetime import datetime
from speech import speak

# Load known faces
known_faces = {
    "person_name ": face_recognition.face_encodings(face_recognition.load_image_file("person_image_path"))[0], # Replace "person_name" with the actual name and "person_image_path" with the image file path
}

# Initialize CSV
csv_filename = "file_path" # Replace with the actual file path where you want to store data
with open(csv_filename, mode='w', newline='') as file:
    csv.writer(file).writerow(["Name", "Time"])

last_detection_time = {}

def log_face_detection(name):
    """Log recognized face into CSV file."""
    if name == "Unknown":
        return
    current_time = datetime.now()
    if name not in last_detection_time or (current_time - last_detection_time[name]).total_seconds() >= 10:
        with open(csv_filename, mode='a', newline='') as file:
            csv.writer(file).writerow([name, current_time.strftime("%Y-%m-%d %H:%M:%S")])
        last_detection_time[name] = current_time

def detect_faces(video_capture):
    """Detect faces in video stream."""
    no_face_counter = 0  

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if face_locations:
            no_face_counter = 0  
            for face_encoding, face_location in zip(face_encodings, face_locations):
                face_distances = face_recognition.face_distance(list(known_faces.values()), face_encoding)
                best_match_index = np.argmin(face_distances)
                name = "Unknown"

                if face_distances[best_match_index] <= 0.6:
                    name = list(known_faces.keys())[best_match_index]
                    speak("Thank you")
                else:
                    speak("Failed")

                log_face_detection(name)
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        else:
            no_face_counter += 1

        cv2.imshow("Face Recognition", frame)

        if no_face_counter >= 30:  
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
