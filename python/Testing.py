import cv2

cap = cv2.VideoCapture("data/data.mp4")


while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Frame', frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()
