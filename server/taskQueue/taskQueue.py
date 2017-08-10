import logging

import server
from app.app import getAppMgr

class TaskQueue(object):
    @staticmethod
    def run(data):
        getAppMgr().get('requestHandMgr').setTaskQueue(data)
        getAppMgr().get('log').warning('data:' + str(data))


getAppMgr().insert('taskQueue', TaskQueue)
