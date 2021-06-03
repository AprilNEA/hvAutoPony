import cv2
import csv
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
        x == 'pony_option/1.jpg': 'R',
        x == 'pony_option/2.jpg': 'FL',
        x == 'pony_option/3.jpg': 'PP',
        x == 'pony_option/4.jpg': 'AP',
        x == 'pony_option/5.jpg': 'TS'
    }
    return matching_dict(id)[True]

def read_csv():
    answer = []
    answer_csv = csv.reader(open('answers3.csv', 'r'))
    for i in answer_csv:
        answer.append(i)
    return answer

template = ['pony_option/0.jpg',
                'pony_option/1.jpg',
                'pony_option/2.jpg',
                'pony_option/3.jpg',
                'pony_option/4.jpg',
                'pony_option/5.jpg']

answer = read_csv()
pony_all = 'pony/'
for i in range(1, 1000000):
    option = 0
    if answer[i] == "A":
        option = 1
    elif answer[i] == "B":
        option = 2
    elif answer[i] == "C":
        option = 3
    files = pony_all + str(i) + ".jpg"
    target = plt.imread(files)
    target = target[..., ::-1]  # RGB --> BGR
    target = target[:20, :700]
    option_list = detect_option(target)
    print(match_answer(option_list[option]))

