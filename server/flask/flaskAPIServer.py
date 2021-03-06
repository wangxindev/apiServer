#建议用tornado与gevent封装flask，以添加并发能力
from flask_api import FlaskAPI, status, exceptions
from flask import request, url_for
import os

from flask_cas import login_required

import server
import server.flask.ApiServerTornado
from app.app import getAppMgr

try:
    loggerInfo = getAppMgr().get('log')
except:
    import logging
    loggerInfo = logging.getLogger()

app = FlaskAPI(__name__)
getAppMgr().insert('flaskApp',app)

task_queue = None
requestHandMgr = getAppMgr().get('RequestHandlerMgr')

class flaskApi(object):

    @staticmethod
    def init():
        app.config['SESSION_TYPE'] = 'filesystem'
        app.config['SECRET_KEY'] = os.urandom(24)

        getAppMgr().get('sqlAlchemyDB').sqlDB_init()
        getAppMgr().get('mycas').cas_init()
        getAppMgr().get('ApiServerAdmin').init_Admin()

    @staticmethod
    def run(queue, flaskQueue, debug=False):
        flaskApi.init()
        global task_queue
        task_queue = queue

        iPort = flaskQueue.get()
        loggerInfo.info('启动服务器监听，监听端口：%s' % iPort)
        server.flask.ApiServerTornado.setTornado(app, iPort)

def push_queue(data):
    global task_queue
    task_queue.put(data)
getAppMgr().insert('push_queue', push_queue)

desc = getAppMgr().get('desc')
notes = getAppMgr().get('notes')

def note_repr(key):
    return {
        '链接': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        '说明': notes[key]
    }

#根目录下应该罗列所有接口的列表以及每个接口的说明
@app.route("/", methods=['GET'])
def notes_list():
    #request.method == 'GET'
    return [note_repr(idx) for idx in sorted(notes.keys())]


@app.route("/ai/api/<string:key>", methods=['POST', 'GET'])
@login_required
def notes_detail(key):

    loggerInfo.info("一个请求访问过来,key:" + key + " method:" + str(request.method) + " requst data:" + str(request.data) + "GET:" + str(request.args))
    retData = None
    retData = requestHandMgr.getResponseData(key, request)
    if not retData is None:
        return retData

    # request.method == 'GET'
    if key not in notes.keys():
        return {"Message": "错误的接口", "Code": 0, "Succeed": False,'V':1.0}
    return note_repr(key)

