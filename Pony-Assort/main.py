import cv2
target = cv2.imread("1.jpg")
target = target[:40, :700] #读取选项栏
template = ['pony_option/0.jpg',
            'pony_option/1.jpg',
            'pony_option/2.jpg',
            'pony_option/3.jpg',
            'pony_option/4.jpg',
            'pony_option/5.jpg']
match_results = []
choices_id = []
for tem in template:
    temp = cv2.imread(tem)
    theight, twidth = temp.shape[:2]
    result = cv2.matchTemplate(target, temp, cv2.TM_SQDIFF_NORMED)#cv2.TM_SQDIFF_NORMED
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
def match_pony(id):
    id = {
        'pony_option/0.jpg': 'RAINBOW DASH',
        'pony_option/1.jpg': 'RARITY',
        'pony_option/2.jpg': 'FLUTTERSHY',
        'pony_option/3.jpg': 'PINKIE PIE',
        'pony_option/4.jpg': 'APPLEJACK',
        'pony_option/5.jpg': 'TWILIGHT SPARKLE'
    }
 return 0



