#-*- coding:utf-8 -*-

"""
本程序需要安装ConcurrentLogHandler包
1.是多进程安全的
2.根据日期分割log文件夹
3.根据大小分割log文件
4.需要调整，请调整配置文件
5.加载配置文件，请使用logging.config.fileConfig("xxx"),需要导入logging.config系统包

1.debug     程序运行时产生的变量等信息
2.info      程序运行状态，代码之行流程等信息
3.warning   程序运行中的重要数据，如用户信息，需要处理的数据等
4.error     不正常的信息
5.critical  错误信息

注意：如果文件达到分割大小，被分割成多个文件，同一天内，程序启动多次，会存在覆盖现象

配置参考文件 log_cfg_file
使用参考
    import classLogMgr
    import logging
    import logging.config

    logging.config.fileConfig("log_cfg_file")

    loggerInfo = logging.getLogger("infoLogger")
    loggerInfo.debug("debug message")
    loggerInfo.info("info message")
    loggerInfo.warn("warn message")
    loggerInfo.error("error message")
    loggerInfo.critical("critical message")

    loggerError = logging.getLogger("errorLogger")
    loggerError.info("Hello world!") 

"""

import time
import os
import logging
try:
    import codecs
except ImportError:
    codecs = None

from cloghandler import ConcurrentRotatingFileHandler

class SafeFileHandler(ConcurrentRotatingFileHandler):
 def __init__(self, filename, mode, encoding=None, delay=0):
     """
     Use the specified filename for streamed logging
     """
     if codecs is None:
         encoding = None

     ConcurrentRotatingFileHandler.__init__(self, filename, mode, encoding, delay)
     self.suffix = "%Y-%m-%d"
     self.suffix_time = ""

 def emit(self, record):
     """
     Emit a record.

     Always check time 
     """
     try:
         if self.check_baseFilename(record):
            self.build_baseFilename()
         ConcurrentRotatingFileHandler.emit(self, record)
     except (KeyboardInterrupt, SystemExit):
         raise
     except:
         self.handleError(record)

 def check_baseFilename(self, record):
     """
     Determine if builder should occur.

     record is not used, as we are just comparing times, 
     but it is needed so the method signatures are the same
     """
     timeTuple = time.localtime()

     if self.suffix_time != time.strftime(self.suffix, timeTuple) or not os.path.exists(self.baseFilename+'.'+self.suffix_time):
         return 1
     else:
         return 0

 def build_baseFilename(self):
     """
     do builder; in this case, 
     old time stamp is removed from filename and
     a new time stamp is append to the filename
     """
     if self.stream:
         self.stream.close()
         self.stream = None

     # remove old suffix
     if self.suffix_time != "":
         self.baseFilename = os.path.dirname(os.path.abspath(self.baseFilename)) + "/../" + os.path.basename(self.baseFilename)

     # add new suffix
     currentTimeTuple = time.localtime()
     self.suffix_time = time.strftime(self.suffix, currentTimeTuple)
     newPath = os.path.dirname(self.baseFilename) + "/" + self.suffix_time
     if not os.path.exists(newPath):
        os.makedirs(newPath)
     self.baseFilename = newPath + "/" + os.path.basename(self.baseFilename)

     if not self.delay:
         self.stream = self._open()

def run():
    import sys
    import logging.config
    logPath = sys.path[0] + '/utilPackage/utilLog/log.config'
    print(logPath)
    logging.config.fileConfig(logPath)

