import urllib.request
import os
import urllib

def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('utf-8')

def get_img(html):
    x = 0        # 声明一个变量赋值
    path = '/'  # 设置图片的保存地址
    if not os.path.isdir(path):
        os.makedirs(path)  # 判断没有此路径则创建
    paths = path + '\\'  # 保存在test路径下
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))  # 打开imgList,下载图片到本地
        x = x + 1
        print('图片开始下载，注意查看文件夹')
    return 0