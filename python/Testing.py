import cv2

cap = cv2.VideoCapture("data/data.mp4")

modelTest = cv2.CascadeClassifier('cars.xml')

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = modelTest.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()
