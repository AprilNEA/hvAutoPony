import requests
a = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000]
for i in a:
    url =
    out = f"/home/g2150499438/pony/{i}.jpeg"

    with open(out, 'wb') as code:
        code.write(down.content)
    print(f"第{i}张马图下载完毕{down}")
