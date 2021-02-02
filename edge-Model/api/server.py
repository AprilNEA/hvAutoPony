from autopony import autopony
from flask import jsonify
from flask import Flask
from flask import request
import json
import time

from flask_cors import cross_origin
app = Flask(__name__)
@app.route('/pony/api', methods=['Post'])
@cross_origin()
def get_tasks():
    start = time.clock()
    useTime = str((int(round((time.clock() - start)* 1000000)))) + 'ms'
    data = request.get_data(as_text=True)
    data = json.loads(str(data))
    base64 = data["base64"]
    answer = autopony(base64)  # 输入base64小马图，输出A\B\C
    back = {
        'return': [
            {'answer': answer,
             'time': useTime
             }
        ]
    }
    return jsonify(back)
if __name__ == '__main__':
    host = input()
    port = input()
    app.run(host=host, port=port)


