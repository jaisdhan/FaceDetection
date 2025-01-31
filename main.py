import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the first webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Webcam - Face Detection', frame)

    # Check if the 'q' key is pressed or the window is closed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Webcam - Face Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
