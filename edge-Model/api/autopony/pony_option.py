import cv2
import matplotlib.pyplot as plt
#matplotlib==3.0.3
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
        x == 'autopony/0.jpg': 'RD',
        x == 'autopony/1.jpg': 'RA',
        x == 'autopony/2.jpg': 'FL',
        x == 'autopony/3.jpg': 'PP',
        x == 'autopony/4.jpg': 'AP',
        x == 'autopony/5.jpg': 'TS'
    }
    return matching_dict(id)[True]

template = ['autopony/0.jpg',
                'autopony/1.jpg',
                'autopony/2.jpg',
                'autopony/3.jpg',
                'autopony/4.jpg',
                'autopony/5.jpg']


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

