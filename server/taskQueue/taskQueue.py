from app.app import getAppMgr

class TaskQueue(object):
    @staticmethod
    def run(data):
        getAppMgr().get('RequestHandlerMgr').setTaskQueue(data)
        getAppMgr().get('log').warning('data:' + str(data))


getAppMgr().insert('taskQueue', TaskQueue)
