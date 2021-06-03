import time
import sqlite3
import base64
import json
import requests
import cv2
import matplotlib.pyplot as plt
from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import cross_origin

def detect_option(target):
    template = ['pony_option/0.jpg',
                'pony_option/1.jpg',
                'pony_option/2.jpg',
                'pony_option/3.jpg',
                'pony_option/4.jpg',
                'pony_option/5.jpg']
    match_results = []
    choices_id = []
    for tem in template:
        temp = cv2.imread(tem)
        result = cv2.matchTemplate(target, temp, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        match_results.append([tem, min_val, min_loc])
    final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
    for match_result in final_result:
        choices_id.append(match_result[0])
    return choices_id

def match_answer(id):
    matching_dict = lambda x: {
        x == 'pony_option/0.jpg': 'RD',
        x == 'pony_option/1.jpg': 'RA',
        x == 'pony_option/2.jpg': 'FL',
        x == 'pony_option/3.jpg': 'PP',
        x == 'pony_option/4.jpg': 'AP',
        x == 'pony_option/5.jpg': 'TS'
    }
    return matching_dict(id)[True]

def option_main(img_path,answer):
    target = plt.imread(img_path)
    target = target[..., ::-1]  # RGB --> BGR
    target = target[:20, :700]
    option_list = detect_option(target)
    ABCoption_list =[]
    for i in option_list:
        ABCoption_list.append(match_answer(i))
    option = ABCoption_list.index(answer)
    if option == 0:
        return "A"
    elif option == 1:
        return "B"
    elif option == 2:
        return "C"
    else:
        return "Wrong"


def container_predict(encoded_image, port_number=8501):
    instances = {
            'instances': [
                    {'image_bytes': {'b64': str(encoded_image)},
                     'key': 'pony'}
            ]
    }
    url = 'http://hk.sukeycz.com:9000/v1/models/default:predict'.format(port_number)
    response = requests.post(url, data=json.dumps(instances))
    return response.json()

def autopony(encoded_image):
    img_data = base64.b64decode(encoded_image)
    file = open('1.jpg', 'wb')
    file.write(img_data)
    file.close()

    start = time.process_time()
    answer_json = container_predict(encoded_image)

    most_prob = 0
    for i in range(1, 6):

        if (answer_json['predictions'][0]['scores'][i] > answer_json['predictions'][0]['scores'][most_prob]):
            most_prob = i
    option = answer_json['predictions'][0]['labels'][most_prob]
    end = time.process_time()
    print(end - start)
    time_pony = str((end - start) * 1000) + "ms"
    print(time_pony)
    return option_main('1.jpg', option), time_pony, option,


app = Flask(__name__)
@app.route('/pony/api/post/<uid>/', methods=['Post'])
@cross_origin()
def do(uid):
    data = request.get_data(as_text=True)
    data = json.loads(str(data))
    word = data["pass"]
    conn = sqlite3.connect('sqlite/pony.db')
    c = conn.cursor()
    cursor = c.execute("SELECT UID,PASS,NAME,GENRE,TIME,TIMESLEFT,TIMESALL from USERPONY")
    for row in cursor:
        if str(row[0]) == str(uid):
            if str(row[1]) == str(word):
                code = 0   #success
                name = row[2]
                genre = row[3]
                time = int(row[4])
                timesleft = int(row[5])
                timesall = int(row[6])
                sql = "UPDATE USERPONY set " + "TIME" + " = " + str(time + 1) + " where " + "UID=" + str(uid)
                c.execute(sql)
                conn.commit()
                sql = "UPDATE USERPONY set " + "TIMESLEFT" + " = " + str(timesleft - 1) + " where " + "UID=" + str(uid)
                c.execute(sql)
                conn.commit()
                sql = "UPDATE USERPONY set " + "TIMESALL" + " = " + str(timesall + 1) + " where " + "UID=" + str(uid)
                c.execute(sql)
                conn.commit()
                break
            else:
                code = 1   #password wrong
        else:
            code = 2        #no account
    if code == 1 or code == 2:
        back = {'return': [{'code': code}]}
        return jsonify(back)
    if int(timesleft) <= 0:
        code = 3
        return {'return': [{'code': code}]}
    base64 = data["base64"]
    answer, time_pony, pony = autopony(base64)
    back = {
        'return': [
            {
                'answer': answer,
                'time_pony': time_pony,
                'pony': pony,
                'time': time,
                'timesleft': timesleft,
                'timesall': timesall,
             }
        ]
    }
    conn.close()
    return jsonify(back)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=True)


