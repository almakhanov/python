import cv2
import sqlite3
import numpy as np

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "classifiers/face_cascade.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = "dataSet"


def getProfie(ID):
    conn = sqlite3.connect("FaceDB.db")
    cmd = "SELECT * FROM User WHERE ID = " + str(ID)
    cursor = conn.execute(cmd)
    user = None
    for row in cursor:
        user = row
    conn.close()
    return user


cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

while cam.isOpened():
    ret, im = cam.read()
    if ret:
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    else:
        continue

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        profile = getProfie(Id)
        if profile is not None:
            cv2.cv.PutText(cv2.cv.fromarray(im), "ID: " + str(profile[0]), (x, y + h + 30), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(im), "Name: " + str(profile[1]), (x, y + h + 60), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(im), "Age: " + str(profile[2]), (x, y + h + 90), font, 255)
            cv2.cv.PutText(cv2.cv.fromarray(im), "Gender: " + str(profile[3]), (x, y + h + 120), font, 255)
        cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
    cv2.imshow('im', im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
