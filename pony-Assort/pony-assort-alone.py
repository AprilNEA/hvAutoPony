# coding:utf-8
#import2 numpy as np
import json
import requests
import os
import cv2
import pprint
import sys
import csv
#File of answer CSV
answer_file = 'answers.csv'

#Directory of specific image 特殊图片位置
path = '/pony/pony_img'
#Directory of all image 所有图片位置
path_all = '/pony/pony_all'

s = []

#Set pony list 设置小马分类及选项
pony_name = [
    'RAINBOW DASH',
    'RARITY',
    'FLUTTERSHY',
    'PINKIE PIE',
    'APPLEJACK',
    'TWILIGHT SPARKLE']
answer_list = ['A', 'B', 'C']
pony_answer_list = csv.reader(open(answer_file,'r'))