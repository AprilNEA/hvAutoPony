import numpy as np
import cv2 as cv
import os
template_path = ['AutoPony-S\pony-Assort\pony_option\0.jpg',
            'AutoPony-S\pony-Assort\pony_option\1.jpg',
            'AutoPony-S\pony-Assort\pony_option\2.jpg',
            'AutoPony-S\pony-Assort\pony_option\3.jpg',
            'AutoPony-S\pony-Assort\pony_option\4.jpg',
            'AutoPony-S\pony-Assort\pony_option\5.jpg'
            ]
target = cv.imread("AutoPony-S/pony-Assort/1.jpg",cv.IMREAD_GRAYSCALE)
target = target[:20, :700] 
match_results = []
choices_id = []
for template_i, template_path in enumerate(template_path):
    template = cv.imread(template_path, cv.IMREAD_GRAYSCALE)
    result = cv.matchTemplate(target, template, cv.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    match_results.append([template_i, min_val, min_loc])

final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
for match_result in final_result:
    choices_id.append(match_result[0])

print(choices_id)
