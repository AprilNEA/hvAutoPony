import wget
for i in range(1, 100001):
    url = "http://wsi.prave.men/pics/" + str(i) + ".jpeg"
    out = '/pony100000/' + str(i) + ".jpeg"
    wget.download(url, out)
    print(url + "Finished")