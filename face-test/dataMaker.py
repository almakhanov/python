import cv2
import sqlite3

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("classifiers/face_cascade.xml")


def insertOrUpdate(Id, Name, Age, Gender):
    conn = sqlite3.connect("FaceDB.db")
    cmd = "SELECT * FROM User WHERE ID =" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1

    if isRecordExist == 1:
        addCmd = "UPDATE User SET Name='" + str(Name) + "', Age='"+str(Age)+"', Gender='"+str(Gender)+"' WHERE ID=" + str(Id)
    else:
        addCmd = "INSERT INTO User(ID,Name,Age,Gender) Values('"+str(Id) + "','" +str(Name) + "','"+str(Age)+"','"+str(Gender)+"')"

    conn.execute(addCmd)
    conn.commit()
    conn.close()


idNum = raw_input('enter your id: ')
name = raw_input('enter your name: ')
age = raw_input('enter your age: ')
gender = raw_input('enter your gender: ')

insertOrUpdate(idNum, name, age, gender)

sampleNum = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # incrementing sample number
        sampleNum = sampleNum + 1
        # saving the captured face in the dataSet folder
        cv2.imwrite("dataSet/User." + idNum + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

        cv2.imshow('frame', img)
    # wait for 100 miliseconds
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum > 49:
        break
cam.release()
cv2.destroyAllWindows()
