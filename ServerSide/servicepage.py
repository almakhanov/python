#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request
import base64
import numpy as np
import cv2
import pdb
import RecognitionPicture

app = Flask(__name__)
tasks = [
    { 
        'id': 1,
        'title': u'Buy groceries',
        'value': u'This is my array[0] value'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'value': u'This is my array[1] value'
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found (error):
    return make_response (jsonify({'error':'not found'}), 404)

@app.route('/todo/api/v1.0/tasks/recognition', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json or not 'value' in request.json:
        abort(400)
    
    # pdb.set_trace()

    sImage = request.json['value']
    missingPadding = len(sImage) % 4
    if (missingPadding != 0):
        sImage += b'='* (4 - missingPadding)
    # img = base64.b64decode(sImage)
    # img = sImage.decode('base64')
    image = base64.standard_b64decode(sImage)
    # img = base64.encodestring(sImage)
    fi = open('my_image.jpg', 'wb')
    fi.write(image)
    fi.close()

    img = cv2.imread('my_image.jpg')
    # img = cv2.resize(imgOriginal, (400, 600))
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    Id, name, age, gender, school, major, description = RecognitionPicture.recg(img)
    taskRespone = {
        'id':Id,
        'title':request.json['title'],
        'status':'success',
        'errorcode':0,
        'name':name,
        'age':age,
        'gender':gender,
        'school':school,
        'major':major,
        'description':description
        
    }
    print (taskRespone)
    return jsonify(taskRespone), 201

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True, host='0.0.0.0')