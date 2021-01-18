# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import urllib.request
import re
import os
import urllib

x = 0        # 声明一个变量赋值
path = 'D:\\pony'  # 设置图片的保存地址
if not os.path.isdir(path):
    os.makedirs(path)  # 判断没有此路径则创建
paths = path + '\\'  # 保存在test路径下
for x in range(48293,1000001):
    imgurl = "http://wsi.prave.men/pics/"+str(x)+".jpeg"
    urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
    print('图片'+str(x)+'开始下载，注意查看文件夹')

