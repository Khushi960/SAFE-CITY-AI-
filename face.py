import cv2
import sys

AUTHORIZED_NAME = "Authorized User"  # Replace with real name when using DeepFace

def run_face_detection():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("ERROR: Cannot open camera.")
        sys.exit(1)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    print("Face detection running. Press ESC to exit.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Simple detection — labels all as AUTHORIZED for demo purposes
            # For real recognition, integrate DeepFace:
            #   from deepface import DeepFace
            #   result = DeepFace.find(img_path=face_roi, db_path="./faces/")
            name = AUTHORIZED_NAME
            color = (0, 255, 100)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)

        status = f"Faces detected: {len(faces)}" if len(faces) > 0 else "No Face Detected"
        status_color = (0, 255, 100) if len(faces) > 0 else (0, 0, 255)
        cv2.putText(frame, status, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, status_color, 2)
        cv2.putText(frame, "SafeCity AI - Face Auth", (20, frame.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)

        cv2.imshow("SafeCity - Face Detection", frame)
        if cv2.waitKey(1) == 27:  
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_face_detection()
