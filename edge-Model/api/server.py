from autopony import autopony

#接受 Base64 转换成 JPEG
'''
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/autopony", methods=["Post"])
def compute():

    return

app.run(host="127.0.0.1", port=5000, debug=True)
'''
pony_path = r'D:\Github\AutoPony-S\pony-Assort\pony_img\pony1000\3.jpg'
print(autopony(pony_path) )#输入小马图，输出A\B\C

