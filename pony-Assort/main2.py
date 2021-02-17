import cv2
import csv
import requests
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
        x == 'pony_option/0.jpg': 'RD',
        x == 'pony_option/1.jpg': 'RA',
        x == 'pony_option/2.jpg': 'FL',
        x == 'pony_option/3.jpg': 'PP',
        x == 'pony_option/4.jpg': 'AP',
        x == 'pony_option/5.jpg': 'TS'
    }
    return matching_dict(id)[True]


def read_csv():
    answer = []
    answer_csv = csv.reader(open('csv/answers3.csv', 'r'))
    for i in answer_csv:
        answer.append(i)
    return answer


rows = []
template = ['pony_option/0.jpg',
            'pony_option/1.jpg',
            'pony_option/2.jpg',
            'pony_option/3.jpg',
            'pony_option/4.jpg',
            'pony_option/5.jpg']
answer = read_csv()
pony_all = 'D://pony10000/'
for i in range(1, 10001):
    if answer[i][0] == "A":
        option = 0
    elif answer[i][0] == "B":
        option = 1
    elif answer[i][0] == "C":
        option = 2
    else:
        option = 4
        print(str(i) + "WRONG!~")
    # files = pony_all + str(i) + ".jpg"
    # files = requests.get(f"http://wsi.prave.men/pics/{i}.jpeg")
    file = open('1.jpg', 'wb')
    file.write(img_data)
    file.close()
    target = plt.imread(files)
    target = target[..., ::-1]  # RGB --> BGR
    target = target[:20, :700]
    target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)
    option_list = detect_option(target)
    if option == 0 or option == 2 or option == 1:
        row = ["gs://cloud-ai-platform-96233cd1-d07c-4fc1-9591-ccde14fdd65b/pony1w/" + str(i) + ".jpg", match_answer(option_list[option])]
    else:
        row = ["gs://cloud-ai-platform-96233cd1-d07c-4fc1-9591-ccde14fdd65b/pony1w/" + str(i) + ".jpg", 'Wrong!']
    print(row)
    rows.append(row)
with open(r'pony.csv', 'w', newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)
