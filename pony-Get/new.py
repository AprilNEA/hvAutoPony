import os
from contextlib import closing
import threading
import requests
import json as js

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

# url 文件夹
json_path = "json/train.json"

# 输出文件夹
out_dir = "train"
# 线程数
thread_num = 400
# http请求超时设置
timeout = 30

if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for img_cla in range(2019):  # 一共2019类，保存在不同文件夹中
    if not os.path.exists(os.path.join(out_dir, str(img_cla))):
        os.makedirs(os.path.join(out_dir, str(img_cla)))


def download(img_url, img_name, img_class):
    if os.path.isfile(os.path.join(os.path.join(out_dir, str(img_class)), img_name)):
        return  ####如果之前下载过这个文件，就跳过
    with closing(requests.get(img_url, stream=True, headers=headers, timeout=timeout)) as r:
        rc = r.status_code
        if 299 < rc or rc < 200:
            print('returnCode%s\t%s' % (rc, img_url))
            return
        content_length = int(r.headers.get('content-length', '0'))
        if content_length == 0:
            print('size0\t%s' % img_url)
            return
        try:
            with open(os.path.join(os.path.join(out_dir, str(img_class)), img_name), 'wb') as f:
                for data in r.iter_content(1024):
                    f.write(data)
        except:
            print('savefail\t%s' % img_url)


def get_img_url_generate():
    imgs = []
    with open(json_path, 'r') as f:
        setting = js.load(f)
        images = setting["images"]
        for img in images:
            imgs = []
            img_url = img['url']
            img_id = img['id']
            img_class = img['class']
            imgs.append(img_url)
            imgs.append(img_id)
            imgs.append(img_class)
            try:
                if img_url:
                    yield imgs
            except:
                break


lock = threading.Lock()


def loop(imgs):
    print('thread %s is running...' % threading.current_thread().name)

    while True:
        try:
            with lock:
                img_url, img_id, img_class = next(imgs)
                print(img_class)
        except StopIteration:
            break
        try:

            download(img_url, img_id, img_class)
        except:
            print('exceptfail\t%s' % img_url)
    print('thread %s is end...' % threading.current_thread().name)


imgs = get_img_url_generate()

for i in range(0, thread_num):
    t = threading.Thread(target=loop, name='LoopThread %s' % i, args=(imgs,))
    t.start()