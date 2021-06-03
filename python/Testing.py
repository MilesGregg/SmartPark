import cv2

cap = cv2.VideoCapture("data/data.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
