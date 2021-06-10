import cv2

from python.SpotGenerator import SpotGenerator

'''import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TestDB"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)'''

image_file = "data/parking_image.png"
generator = SpotGenerator((255, 255, 255), image_file)
generator.generate_spots()


'''cap = cv2.VideoCapture("data/data.mp4")


while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Frame', frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()'''
