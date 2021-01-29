import cv2
import csv
import os
import matplotlib.pyplot as plt

def detect_option(target):
    match_results = []
    choices_id = []
    for tem in template:
        temp = cv2.imread(tem, cv2.IMREAD_GRAYSCALE)
        result = cv2.matchTemplate(target, temp, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        match_results.append([tem, min_val, min_loc])
    final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
    for match_result in final_result:
        choices_id.append(match_result[0])
    return choices_id

def match_answer(id):
    matching_dict = lambda x: {
        x == 'pony_option/20.jpg': 'RD',
        x == 'pony_option/21.jpg': 'RA',
        x == 'pony_option/22.jpg': 'FL',
        x == 'pony_option/23.jpg': 'PP',
        x == 'pony_option/24.jpg': 'AP',
        x == 'pony_option/25.jpg': 'TS'
    }
    return matching_dict(id)[True]

def read_csv():
    answer = []
    answer_csv = csv.reader(open('D:\Github\AutoPony-S\pony-Assort\csv\\answers2.csv', 'r'))
    for i in answer_csv:
        answer.append(i)
    return answer

rows = []
template = ['pony_option/20.jpg',
                'pony_option/21.jpg',
                'pony_option/22.jpg',
                'pony_option/23.jpg',
                'pony_option/24.jpg',
                'pony_option/25.jpg']
answer = read_csv()
pony_all = 'D:/Github/AutoPony-S/pony-Assort/pony_img/pony1000/'
for i in range(1, 1001):
    option = 1
    if answer[i][0] == "A":
        option = 0
    elif answer[i][0] == "B":
        option = 1
    elif answer[i][0] == "C":
        option = 2
    else:
        print(str(i) + "WRONG!~")
    files = pony_all + str(i) + ".jpg"
    target = plt.imread(files)
    target = target[..., ::-1]  # RGB --> BGR
    target = target[:40, :700]
    target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)
    option_list = detect_option(target)
    row = ["gs://pony1000testus/" + str(i) + ".jpg", match_answer(option_list[option])]
    if i == 3:
        print(answer[i][0])
        print(option_list)
        print(row)
    rows.append(row)
with open(r'D:\Github\AutoPony-S\pony-Assort\resule\pony1000gdk.csv', 'w', newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)