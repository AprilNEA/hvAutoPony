import base64
import io
import json
import requests
from pony_option import *

def container_predict(image_file_path, image_key, port_number=8501):
    with io.open(image_file_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    instances = {
            'instances': [
                    {'image_bytes': {'b64': str(encoded_image)},
                     'key': image_key}
            ]
    }
    url = 'http://hk.sukeycz.com:9000/v1/models/default:predict'.format(port_number)
    response = requests.post(url, data=json.dumps(instances))
    return response.json()
def autopony(pony_path): #输入小马图，输出A\B\C
    #pony_path = r'D:\Github\AutoPony-S\pony-Assort\pony_img\pony1000\3.jpg'
    answer_json = container_predict(pony_path,"pony_img")
    most_prob = 0
    for i in range(1,6):
        print(answer_json['predictions'][0]['scores'][i])
        print(answer_json['predictions'][0]['scores'][most_prob])
        if (answer_json['predictions'][0]['scores'][i] > answer_json['predictions'][0]['scores'][most_prob]):
            most_prob = i
    option = answer_json['predictions'][0]['labels'][most_prob]
    #print(option)
    #print(option_main(pony_path,option))
    return option_main(pony_path,option)