import _thread
import wget

# 下载函数
def download_main(number,start,end):
   for i in range(start, end+1):
      url = "http://wsi.prave.men/pics/" + str(i) + ".jpeg"
      out = '/pony100000/' + str(i) + ".jpeg"
      wget.download(url, out)
      print(url + "Finished")
      if i == end:
         print("线程" + str(number) + ": 从" + str(start) + "到" + str(end) + "已完成")

# 创建多个线程
try:
   num = 1
   for i in range(1,100000,10000):
      _thread.start_new_thread(download_main, (num, i, i+10000,))
      num = num + 1
except:
   print ("Error: 无法启动多线程下载")

while 1:
   pass