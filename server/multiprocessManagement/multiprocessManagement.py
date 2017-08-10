#标准模块
import time
import multiprocessing

from app.app import getAppMgr

from server.flask.flaskAPIServer import flaskApi

loggerInfo = getAppMgr().get('log')

#个人模块
from server.config import parameters

class multiprocessManagementObj(object):
    def __init__(self):
        self.queue = multiprocessing.Queue()
        self.flaskQueue = multiprocessing.Queue()
        self.flaskProcessing = []
        self.taskPoolMgr = None
        self.pool = None
        self.nginxPort = parameters.NGINX_PORT


    def __flaskAPIfunc(self, queue, flaskQueue):
        loggerInfo.info('flaskAPI进程拉起成功')
        self.queue = queue
        self.flaskQueue = flaskQueue
        getAppMgr().insert('flask-queue', queue)
        getAppMgr().insert('flask-flaskQueue', flaskQueue)
        try:
            flaskApi.run(self.queue, self.flaskQueue, True)
        except:
            loggerInfo.info('flaskAPI业务启动失败')

    def initFlaskServer(self):
        self.__initFlaskProcessing()

    def initPorlServer(self):
        self.__initPool()

    #初始化flask API server 的进程
    def __initFlaskProcessing(self, flaskServer = None):
        loggerInfo.info('尝试拉起flaskAPI进程')
        try:
            if flaskServer == None:
                loggerInfo.info('拉起flaskAPI所有进程')
                for i in range(parameters.FLASK_SERVER_COUNT):
                    iPort = self.nginxPort-i-1
                    self.flaskQueue.put(iPort)
                    flaskServerProcessing = multiprocessing.Process(target=self.__flaskAPIfunc, args=(self.queue,self.flaskQueue,))
                    flaskServerProcessing.start()
                    self.flaskProcessing.append({'port':iPort,'process':flaskServerProcessing})
            else:
                loggerInfo.info('拉起flaskAPI端口为%d进程'%flaskServer['port'])
                self.flaskQueue.put(flaskServer['port'])
                flaskServer['process'] = multiprocessing.Process(target=self.__flaskAPIfunc, args=(self.queue,self.flaskQueue,))
                flaskServer['process'].start()

        except:
            loggerInfo.info('flaskAPI进程拉起失败')
            self.flaskProcessing = []

    #任务管理队列的进程池
    def __taskRun(self, queue):
        loggerInfo.info('__taskRun 业务队列管理进程成功拉起，尝试拉起进程池')
        try:
            self.queue = queue
            self.pool = multiprocessing.Pool(processes=parameters.QUEUE_TASK_COUNT)
            loggerInfo.info('业务进程池拉起成功,开始分发业务')
        except:
            loggerInfo.info('业务进程池拉起失败')
            self.pool = None
            self.taskPoolMgr = None

        loggerInfo.info("开始业务循环派发（从消息队列中取消息）")
        while True:
            loggerInfo.info("获取消息队列中的一个消息")
            data = self.queue.get()
            loggerInfo.debug("消息：" + str(data))
            loggerInfo.info("获取消息结束")
            loggerInfo.info("发送消息到具体业务处理方法")
            self.pool.apply_async(getAppMgr().get('taskQueue').run, (data,))
            loggerInfo.info("业务处理结束")

    #初始化任务管理队列进程
    def __initPool(self):
        loggerInfo.info('__initPool 拉起业务队列管理进程')
        try:
            self.taskPoolMgr = multiprocessing.Process(target=self.__taskRun, args=(self.queue,))
            self.taskPoolMgr.start()
        except:
            self.taskPoolMgr = None

    #守护进程，每两秒检查一次，如果flaskAPI server 挂掉，则启动, 如果任务队列进程挂掉，则启动任务队列进程
    def start(self):
        while True:
            try:
                for flaskServer in self.flaskProcessing:
                    if flaskServer['process'] is None or not flaskServer['process'].is_alive():
                        loggerInfo.info('拉起flaskAPI业务服务')
                        self.__initFlaskProcessing(flaskServer)
                if self.taskPoolMgr is None:
                    loggerInfo.info('拉起业务进程池服务')
                    self.__initPool()
            except:
                loggerInfo.info("程序进程拉起失败")
            time.sleep(parameters.DAEMON_PROCESS_DETECTION_TIME)


def run():
    loggerInfo.info("程序启动")
    multiprocessMgr = multiprocessManagementObj()
    multiprocessMgr.initFlaskServer()
    multiprocessMgr.initPorlServer()
    multiprocessMgr.start()

getAppMgr().insert('multiprocessManagementRun', run)

if __name__ == '__main__':
    run()

