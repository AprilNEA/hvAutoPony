import os
import urllib
import urllib.request
from multiprocessing.pool import ThreadPool
from time import time

import requests

urls=[
("Event1"，"https://www.python.org/events/python-events/805/"),
("Event2"，"https://www.python.org/events/python-events/801/"),
("Event3"，"https://www.python.org/events/python-events/802/")，
("Event4"，"https://www.python.org/events/python-events/803/")，
("Event5"，"https://www.python.org/events/python-events/804/")
]
def url_response(url):
	path,url='D:\Github\AutoPony-S\pony-Assort\pony_all',url
	r=requests.get(url,stream=True)
	with open(path,'wb')as f:
		for ch in f:
			f.write(ch)

start=time()
for x in urls:
	url_response(x)
print(f"time to download:{time()-start}")

def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')


def get_img():
    #reg = r'https://[^\s]*?\.jpg'
    #imgre = re.compile(reg)  # 转换成一个正则对象
    #imglist = imgre.findall(html)  # 表示在整个网页过滤出所有图片的地址，放在imgList中
    x = 0        # 声明一个变量赋值
    path = 'D:\\pony'  # 设置图片的保存地址
    if not os.path.isdir(path):
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'  # 保存在test路径下
    for x in range(0,10):
        imgurl = "http://wsi.prave.men/pics/"+x+".jpeg"
        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
        print('图片'+x+'开始下载，注意查看文件夹')
    return imglist



print(get_img())  # 从网页源代码中分析下载保存图片
