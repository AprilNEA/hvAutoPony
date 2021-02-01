import requests
for i in range(1, 20001):
    url = "http://wsi.prave.men/pics/" + str(i) + ".jpeg"
    out = 'pony20000/' + str(i) + ".jpeg"
    down = requests.get(url)
    open('out', 'wb').write(down.content)
    print(url + "Finished")