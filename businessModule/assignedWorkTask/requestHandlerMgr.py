import logging

from app.app import getAppMgr

def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class RequestHandlerMgr(object):
    def __init__(self):
        self.RequestHandlerList = []

    def register(self, classRequestHandler):
        self.RequestHandlerList.append(classRequestHandler)

    def getResponseData(self, key, request):
        for hd in self.RequestHandlerList:
            data = None
            if hd.key == key:
                data = hd.run(key, request)
            if not data is None:
                return data
        return None

    def setTaskQueue(self, data):
        for hd in self.RequestHandlerList:
            if data['key'] == hd.key:
                hd.taskQueue(data['data'])

# getAppMgr().get('rigister').rigister()
getAppMgr().insert('RequestHandlerMgr',RequestHandlerMgr())
