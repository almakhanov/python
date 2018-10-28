import cv2
import numpy as np


def recg(im):
    global Id, name, age, gender, school, major
    recognizer = cv2.createLBPHFaceRecognizer()
    recognizer.load('Trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    while True:
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                if (Id == 1):
                    Id = "1"
                    name = 'Vu The Dung'
                    age = 21
                    gender = 'Male'
                    school = 'Dai hoc cong nghe thong tin'
                    major = 'Khoa hoc may tinh'
                    description = ''
                elif (Id == 2):
                    Id = "2"
                    name = 'Tran Quoc Long'
                    age = 21
                    gender = 'Male'
                    school = 'Dai hoc cong nghe thong tin'
                    major = 'Khoa hoc may tinh'
                    description = 'Trum everything'
                elif Id == 3:
                    Id = "3"
                    name = 'Vu The Dung'
                    age = 21
                    gender = 'Male'
                    school = 'Dai hoc cong nghe thong tin'
                    major = 'Khoa hoc may tinh'
                    description = ''

                elif Id == 4:
                    Id = "4"
                    name = 'Taylor Swift'
                    age = 21
                    gender = 'Female'
                    school = 'Unknown'
                    major = 'Singer'
                    description = 'Country music'

                elif Id == 5:
                    Id = "5"
                    name = 'Ngo Kinh'
                    age = 43
                    gender = 'Male'
                    school = 'Unkown'
                    major = 'Actor'
                    description = 'VIPPPPPPPPPP'
                elif Id == 6:
                    Id = "6"
                    name = 'Chau Kiet Luan'
                    age = 38
                    gender = 'Male'
                    school = 'Unkown'
                    major = 'Singer'
                    description = ''

                else:
                    Id = "Null"
                    name = 'Null'
                    age = 00
                    gender = 'Null'
                    school = 'Null'
                    major = 'Null'
                    description = 'Null'
            else:
                Id = "nofill"
                name = 'Null'
                age = 00
                gender = 'Null'
                school = 'Null'
                major = 'Null'
                description = 'Null'

            cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
            print(str(Id))
            break;
            # im = cv2.resize(im, (400,600))
            # cv2.imshow('im',im) 
        if cv2.waitKey(0):
            break
    cv2.destroyAllWindows()
    return Id, name, age, gender, school, major, description
