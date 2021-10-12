import os

from flask_cors import CORS
from flask import Flask, jsonify,session, redirect, url_for, escape
from flask import request

#实例化，可视为固定格式
app = Flask(__name__)
CORS(app, supports_credentials=True)
#如果app.secret_key未设置,则Flask将不允许你设置或访问会话字典。
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

data={}

#检测服务器连接成功
@app.route('/connect', methods=["get"])
def connect():
    ret = {'code': 0,'message':'succeed'}
    return jsonify(ret)

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    
    app.run(host="0.0.0.0", port=3000)