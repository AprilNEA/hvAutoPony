import wget

# 马图下载
def download_main(number,start,end):
   for i in range(start, end+1):
      url = "http://wsi.prave.men/pics/" + str(i) + ".jpeg"
      out = '/pony100000/' + str(i) + ".jpeg"
      wget.download(url, out)
      print(url + " Finished")
