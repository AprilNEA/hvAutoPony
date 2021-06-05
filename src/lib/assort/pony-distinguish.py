import cv2
#import matplotlib.pyplot as plt
import base64

import numpy as np

files = r'D:\Github\hvAutoPony\public\pony_img\pony1000\3.jpg'

img_file = open(files, 'rb')  # 二进制打开图片文件
img_b64encode = base64.b64encode(img_file.read())  # base64编码
img_file.close()  # 文件关闭
img_b64decode = base64.b64decode(img_b64encode)  # base64解码
# fromstring => formbuffer
img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
target = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式


#arget = plt.imread(files)
#target = target[..., ::-1]  # RGB --> BGR
target = target[:40, :700]
target = cv2.cvtColor(target, cv2.COLOR_RGB2GRAY)
OPTION_IMG_ADDRESS = "public/pony_option"
template = [f'{OPTION_IMG_ADDRESS}/20.jpg',
            f'{OPTION_IMG_ADDRESS}/21.jpg',
            f'{OPTION_IMG_ADDRESS}/22.jpg',
            f'{OPTION_IMG_ADDRESS}/23.jpg',
            f'{OPTION_IMG_ADDRESS}/24.jpg',
            f'{OPTION_IMG_ADDRESS}/25.jpg']
match_results = []
choices_id = []
for tem in template:
    temp = cv2.imread(tem, cv2.IMREAD_GRAYSCALE)
    theight, twidth = temp.shape[:2]
    result = cv2.matchTemplate(target, temp, cv2.TM_SQDIFF_NORMED)
    #cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    strmin_val = str(min_val)
    cv2.rectangle(target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
    match_results.append([tem, min_val, min_loc])
    cv2.imshow("MatchResult----MatchingValue=" + strmin_val, target)
    cv2.waitKey()
    cv2.destroyAllWindows()
final_result = sorted(sorted(match_results, key=lambda x: x[1])[:3], key=lambda x: x[2][0])
for match_result in final_result:
    choices_id.append(match_result[0])
print(match_results)
print(final_result)
print(choices_id)
def matching_lambda(id):
    matching_dict = lambda x: {
        x == 'pony_option/20.jpg': 'RAINBOW DASH',
        x == 'pony_option/21.jpg': 'RARITY',
        x == 'pony_option/22.jpg': 'FLUTTERSHY',
        x == 'pony_option/23.jpg': 'PINKIE PIE',
        x == 'pony_option/24.jpg': 'APPLEJACK',
        x == 'pony_option/25.jpg': 'TWILIGHT SPARKLE'
    }
    return matching_dict(id)[True]
for id in choices_id:
    print(matching_lambda(id))
