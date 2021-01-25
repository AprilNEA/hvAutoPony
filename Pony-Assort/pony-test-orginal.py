from PIL import Image # abc
import numpy as np
import os
import cv2 as cv2
import pprint
import sys

#Set pony list 设置小马分类及选项
#RAINBOW DASH 0
#RARITY 1
#FLUTTERSHY 2
#PINKIE PIE 3
#APPLEJACK 4
#TWILIGHT SPARKLE 5
#pony_name = ['RAINBOW DASH', 'RARITY', 'FLUTTERSHY', 'PINKIE PIE', 'APPLEJACK', 'TWILIGHT SPARKLE']
#answer_list = ['A', 'B', 'C']

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

detect_option('D:/Github/AutoPony-S/pony-Assort/1.jpg')