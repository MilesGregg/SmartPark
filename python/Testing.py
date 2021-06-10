import cv2
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TestDB"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

'''cap = cv2.VideoCapture("data/data.mp4")


while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Frame', frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()'''
