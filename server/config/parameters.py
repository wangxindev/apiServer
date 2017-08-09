
NGINX_PORT = 3330 #nginx 分发时候占用的端口
FLASK_SERVER_COUNT = 24 #这里会根据nginx占用的端口递减占用端口
QUEUE_TASK_COUNT = 1 #离线任务队列进程数量
DAEMON_PROCESS_DETECTION_TIME=2 #守护进程检测服务器进程状态的时间间隔

SERVER_STATS_DEBUG = False #服务器是否处于调试状态

IS_HTTPS = True #是否开启https

