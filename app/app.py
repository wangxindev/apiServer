#
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class AppMgr(object):
    def __init__(self):
        self.__values = {}

    def insert(self,key=None, value=None):

        if key == None:
            raise NameError('key is None')
        if value == None:
            raise NameError('value is None')
        if not isinstance(key, str):
            raise NameError('key is not str')
        if key in self.__values.keys():
            raise NameError('key exist')

        print('------> app insert %s'%key)
        self.__values[key] = value

    def get(self, key):
        if key == None:
            raise NameError('key is None')
        if not isinstance(key, str):
            raise NameError('key is not str')

        if key in self.__values.keys():
            return self.__values[key]
        else:
            raise NameError('key not exist')

    def getKeys(self):
        return self.__values.keys()


appMgr = AppMgr()

def getAppMgr():
    return appMgr

import sys
import logging.config
logPath = sys.path[0] + '/utilPackage/utilLog/log.config'
logging.config.fileConfig(logPath)
loggerInfo = logging.getLogger('loggerInfo')
getAppMgr().insert('log',loggerInfo)
