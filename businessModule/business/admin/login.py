from app.app import getAppMgr

loggerInfo = getAppMgr().get('log')
RequestHandlerBase = getAppMgr().get('RequestHandlerBase')

class LoginApiRequestHandler(RequestHandlerBase):

    def __init__(self):
        RequestHandlerBase.init(self, "login", None)

    def run(self, key, request):
        return {"Message": "接收到数据" + str(request.data), "Code": 0, "Succeed": True, 'V': 1.0, "data": str(request.args)}

    def taskQueue(self, data):
        print("hahahah 我处理了这个离线任务 data=%s"%str(data))