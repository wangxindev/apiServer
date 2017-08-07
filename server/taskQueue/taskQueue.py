import logging

import server


loggerInfo = logging.getLogger("infoLogger")

requestHandMgr = server.RequestHandlerMgr()

def taskQueue(data):
    requestHandMgr.setTaskQueue(data)
    loggerInfo.warning('data:' + str(data))