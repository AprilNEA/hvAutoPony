
from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import cross_origin
import json
import time
import base64
import json
import requests
import cv2
import matplotlib.pyplot as plt

def detect_option(target):
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

template = ['pony_option/0.jpg',
                'pony_option/1.jpg',
                'pony_option/2.jpg',
                'pony_option/3.jpg',
                'pony_option/4.jpg',
                'pony_option/5.jpg']

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


def container_predict(encoded_image, image_key, port_number=8501):
   # with io.open(image_file_path, 'rb') as image_file:
   #     encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    instances = {
            'instances': [
                    {'image_bytes': {'b64': str(encoded_image)},
                     'key': image_key}
            ]
    }
    url = 'http://hk.sukeycz.com:9000/v1/models/default:predict'.format(port_number)
    response = requests.post(url, data=json.dumps(instances))
    return response.json()
def autopony(encoded_image): #输入base64小马图，输出A\B\C
    imgdata = base64.b64decode(encoded_image)
    file = open('1.jpg', 'wb')
    file.write(imgdata)
    file.close()
    print(encoded_image)
    answer_json = container_predict(encoded_image,"pony_img")
    most_prob = 0
    for i in range(1, 6):
        #print(answer_json['predictions'][0]['scores'][i])
        #print(answer_json['predictions'][0]['scores'][most_prob])
        if (answer_json['predictions'][0]['scores'][i] > answer_json['predictions'][0]['scores'][most_prob]):
            most_prob = i
    option = answer_json['predictions'][0]['labels'][most_prob]
    #print(option)
    #print(option_main(pony_path,option))
    return option_main('1.jpg',option)


app = Flask(__name__)
@app.route('/pony/api', methods=['Post'])
@cross_origin()
def get_tasks():
    start = time.clock()
    useTime = str((int(round((time.clock() - start)* 1000000)))) + 'ms'
    data = request.get_data(as_text=True)
    data = json.loads(str(data))
    base64 = data["base64"]
    answer = autopony(base64)  # 输入base64小马图，输出A\B\C
    back = {
        'return': [
            {'answer': answer,
             'time': useTime
             }
        ]
    }
    return jsonify(back)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81)


