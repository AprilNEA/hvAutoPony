from autopony import autopony
from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/api', methods=['Post'])
def get_tasks():
    a = request.values.get("a")
    # 接受 Base64 转换成 JPEG
    # pony_path = r'D:\Github\AutoPony-S\pony-Assort\pony_img\pony1000\3.jpg'
    # print(autopony(pony_path) )#输入小马图，输出A\B\C
    return a

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)


