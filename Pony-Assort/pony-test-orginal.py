#from PIL import Image
import numpy as np
import json
import requests
import os
import cv2
import pprint
import sys

#Set pony list 设置小马分类及选项
#RAINBOW DASH 0
#RARITY 1
#FLUTTERSHY 2
#PINKIE PIE 3
#APPLEJACK 4
#TWILIGHT SPARKLE 5
pony_name = ['RAINBOW DASH', 'RARITY', 'FLUTTERSHY', 'PINKIE PIE', 'APPLEJACK', 'TWILIGHT SPARKLE']
answer_list = ['A', 'B', 'C']

#Detect Options 检测选项
def detect_option(target_path, template_path=None):
    template_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pony/pony_option')
    if not template_path:
        template_path = [os.path.join(template_root, '0.jpg'),
            os.path.join(template_root, '1.jpg'),
            os.path.join(template_root, '2.jpg'),
            os.path.join(template_root, '3.jpg'),
            os.path.join(template_root, '4.jpg'),
            os.path.join(template_root, '5.jpg')]

    #Read target imaged 读取图片上方选项
    target = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE) #以灰度模式加载图片
    target = target[:20, :700] #读取选项栏
    match_results = []
    choices_id = []
    for template_i, template_path in enumerate(template_path):
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        match_results.append([template_i, min_val, min_loc])
    
    #Get final result 获取答案
    final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
    for match_result in final_result:
        choices_id.append(match_result[0])
    return choices_id

def match_result(responses, options):
    obj = json.loads(responses.text)
    find_option = np.argmax(obj['predictions'][0])
    get_answer = answer_list[options.index(find_option)]
    if responses.status_code == 200:
        status = 'success'
        return_response = {'is_chocie': True, 'status': status, 'answer': get_answer}
    else:
        status = 'failed'
        return_response = {'is_chocie': False, 'status': status, 'reason': responses.error}
    result_info = json.dumps(return_response)
    return result_info
def detect_pony(target_path):
    f = csv.reader(open('pony-Assort\pony1000.csv','r'))
    
path = 'pony-Assort\pony_option'#Directory of specific image 特殊图片位置
path_all = 'pony-Assort\pony_img\pony1000'#Directory of all image 所有图片位置
s = []
#Get all file names in the directory 获取目录下所有文件名
files = os.listdir(path_all)
#print(files)
#test_script(path_all, files)
files = os.listdir(path)
#Start detect 开始鉴定
#response = detect_pony(path + '/' + filename)
""" for filename in files:
    print(path + '/' + filename)
    get_option = detect_option(path + '/' + filename)
    #result_pony = match_result(response, get_option)   
    print(get_option) """
get_option = detect_option(r'pony-Assort/0.jpg')
print(get_option)