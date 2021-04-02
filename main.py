#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: Green Sulley
# @license: AGPL-3.0 License
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: api.py
# @time: 2021/6/4 22:54
# @desc:
import base64
import json
import cv2
import numpy as np
import requests


def detect_option(target):
    template = {
        "RD": 'pony_option/RD.jpg',
        "RA": 'pony_option/RA.jpg',
        "FL": 'pony_option/FL.jpg',
        "PP": 'pony_option/PP.jpg',
        "AP": 'pony_option/AP.jpg',
        "TS": 'pony_option/TS.jpg'
    }
    match_results = []
    choices_id = []
    for pony_name, tem in template.items():
        temp = cv2.imread(tem)
        result = cv2.matchTemplate(target, temp, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        match_results.append([pony_name, min_val, min_loc])
    final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
    for match_result in final_result:
        choices_id.append(match_result[0])
    return choices_id


def option_main(img_b64decode, answer):
    img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
    target = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)
    target = target[:20, :700]
    option_list = detect_option(target)
    # print(option_list)
    option = option_list.index(answer)
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
                    {'image_bytes': {'b64': encoded_image},
                     'key': 'pony'}
            ]
    }
    url = 'http://119.28.92.228:8501/v1/models/default:predict'.format(port_number)
    response = requests.post(url, data=json.dumps(instances))
    answer_json = response.json()
    most_prob = 0
    for i in range(1, 6):
        if (answer_json['predictions'][0]['scores'][i] > answer_json['predictions'][0]['scores'][most_prob]):
            most_prob = i
    option = answer_json['predictions'][0]['labels'][most_prob]
    return option


def autopony(encoded_image):
    img_data = base64.b64decode(encoded_image)
    option = container_predict(encoded_image)
    return option_main(img_data, option), option



if __name__ == '__main__':
    img_src = 'https://z3.ax1x.com/2021/06/06/2UPjCd.jpg'
    img = requests.get(img_src)
    base64Data = base64.b64encode(img.content).decode('utf-8')
    r = autopony(base64Data)
    print(r)
