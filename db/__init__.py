import os

from app.app import getAppMgr

path = os.path.join(os.path.abspath("."))
getAppMgr().insert('path', path)

dbpath = path + 'db/'
getAppMgr().insert('dbpath', dbpath)

