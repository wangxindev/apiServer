import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from server.config import parameters

def setTornado(app, iPort):
    if parameters.IS_HTTPS:
        http_server = HTTPServer(WSGIContainer(app), ssl_options={
            "certfile": os.path.join(os.path.abspath("."), "utilPackage/utilSSL/server.crt"),
            "keyfile": os.path.join(os.path.abspath("."), "utilPackage/utilSSL/server.key"),
        })
    else:
        http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(iPort)  # flask默认的端口
    IOLoop.instance().start()