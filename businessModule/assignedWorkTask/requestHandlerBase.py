from app.app import getAppMgr

loggerInfo = getAppMgr().get('log')

class RequestHandlerBase(object):

    def init(self, key, request):
        self.key = key
        self.request = request

    def run(self, key, request):
        return None

    def pushData(self,data):
        tempData = {}
        tempData['key'] = self.key
        tempData['data'] = data
        getAppMgr().get('push_queue')(tempData)

    def taskQueue(self, data):
        loggerInfo.warning('没有复写taskQueue函数处理离线业务 key = %s, data = %s'%(str(self.key), str(data)))
        return None

getAppMgr().insert('RequestHandlerBase', RequestHandlerBase)