import platform
import os
import argparse
import sys


import server


parser = argparse.ArgumentParser(description="广告系统系统参数帮助")
parser.add_argument("-s", "--stop", help="停止广告服务器", action="store_true")
parser.add_argument("-r", "--run", help="启动广告服务器", action="store_true")
parser.add_argument("-e", "--echo", help="显示一些位置执行命令等信息", action="store_true")

args = parser.parse_args()

runStr = 'source activate apiServer && nohup python ' + str(sys.path[0]) + '/main.py >/dev/null &'

if args.stop:
    os.system("ps  -ef|grep serverMgr.py|grep -v grep|grep wangxin|grep python|awk '{print $2}'|xargs kill -9")

if args.run:
    os.system("ps  -ef|grep serverMgr.py|grep -v grep|grep wangxin|grep python|awk '{print $2}'|xargs kill -9")
    os.system(runStr)

if args.echo:
    print('-'*50)
    print('server path      ==> %s'%str(sys.path[0]))
    print('run server cmd   ==> %s'%runStr)
    print('-'*50)
    print('env cmd          ==> source activate apiServer')
    print('-'*50)

if __name__ == '__main__':
    server.run()


