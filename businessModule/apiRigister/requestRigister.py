from businessModule.business.test.test import testRequestHandler
from businessModule.business.adInfoComposing.adComposingApi import AdComposingApiRequestHandler
from businessModule.business.admin.login import LoginApiRequestHandler

from app.app import getAppMgr

class RequestRigister(object):

    @staticmethod
    def rigister():
        testApi = testRequestHandler()
        getAppMgr().get('RequestHandlerMgr').register(testApi)

        adApi = AdComposingApiRequestHandler()
        getAppMgr().get('RequestHandlerMgr').register(adApi)

        loginApi = LoginApiRequestHandler()
        getAppMgr().get('RequestHandlerMgr').register(loginApi)

    @staticmethod
    def init():
        getAppMgr().insert('rigister', RequestRigister)


RequestRigister.rigister()