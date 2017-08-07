import logging

from server.assignedWorkTask.requestHandlerBase import RequestHandlerBase

from businessModule.business.adInfoComposing.createADInfoByParseXml import parseXmlAndGetAdInfo

loggerInfo = logging.getLogger("infoLogger")

class AdComposingApiRequestHandler(RequestHandlerBase):

    def __init__(self):
        RequestHandlerBase.init(self, "adComposingApi", None)

    def run(self, key, request):
        if isinstance(request.data, dict):
            loggerInfo.warning("get data:" + str(request.data))
            tempdata = parseXmlAndGetAdInfo('sku88888888', '0')
            loggerInfo.warning("send data:" + str(request.data))
            RequestHandlerBase.pushData(self, tempdata)
            return {"Message": "接收到数据", "Code": 0, "Succeed": True, 'V': 1.0, "data": tempdata}
        else:
            return {"Message": "请传递正确的json数据", "Code": 0, "Succeed": False, 'V': 1.0}

    def taskQueue(self, data):
        print("hahahah 我处理了这个离线任务 data=%s"%str(data))
