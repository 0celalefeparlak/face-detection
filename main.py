import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)

face_detected = False

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=6, minSize=(32, 32))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Here!', (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        face_detected = True

    if face_detected is True:
        cv2.putText(frame, 'Face is Detected', (12, 32), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, 'Face is Not Detected', (12, 32), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    face_detected = False

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
