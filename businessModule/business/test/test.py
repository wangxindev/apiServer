# import logging
#
# from server.assignedWorkTask.requestHandlerBase import RequestHandlerBase
#
# loggerInfo = logging.getLogger("infoLogger")
#
# class testRequestHandler(RequestHandlerBase):
#
#     def __init__(self):
#         RequestHandlerBase.init(self, "test", None)
#
#     def run(self, key, request):
#         if key == self.key:
#             if isinstance(request.data, dict):
#                 # push_queue(request.data)
#                 if 'title' in request.data:
#                     loggerInfo.warning("get data:" + str(request.data))
#                     loggerInfo.warning("send data:" + str(request.data))
#                     return {"Message": "接收到数据", "Code": 0, "Succeed": True, 'V': 1.0, "data": request.data}
#                 else:
#                     RequestHandlerBase.pushData(self, "hahahaha")
#                     return {"Message": "请传递Title数据", "Code": 0, "Succeed": False, 'V': 1.0}
#             else:
#                 return {"Message": "请传递正确的json数据", "Code": 0, "Succeed": False, 'V': 1.0}
#         else:
#             return None

import logging

from server.assignedWorkTask.requestHandlerBase import RequestHandlerBase

loggerInfo = logging.getLogger("infoLogger")

class testRequestHandler(RequestHandlerBase):

    def __init__(self):
        RequestHandlerBase.init(self, "test", None)

    def run(self, key, request):
        if isinstance(request.data, dict):
            if 'title' in request.data:
                loggerInfo.warning("get data:" + str(request.data))
                return {"Message": "接收到数据", "Code": 0, "Succeed": True, 'V': 1.0, "data": request.data}
            else:
                RequestHandlerBase.pushData(self, "hahahaha")
                return {"Message": "请传递Title数据", "Code": 0, "Succeed": False, 'V': 1.0}
        else:
            return {"Message": "请传递正确的json数据", "Code": 0, "Succeed": False, 'V': 1.0}

    def taskQueue(self, data):
        print("hahahah 我处理了这个离线任务 data=%s"%str(data))
