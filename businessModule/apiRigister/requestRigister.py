# import src.RequestHandler.googleApiRequestHandler
# import src.RequestHandler.adText
#
# def rigister(requestHandMgr):
#     googleApi = src.RequestHandler.googleApiRequestHandler.GoogleApiRequestHandler()
#     requestHandMgr.register(googleApi)
#
#     adTextApi = src.RequestHandler.adText.AdTextApiRequestHandler()
#     requestHandMgr.register(adTextApi)


import businessModule.business.test.test
from businessModule.business.test.test import testRequestHandler
from businessModule.business.adInfoComposing.adComposingApi import AdComposingApiRequestHandler

def rigister(requestHandMgr):
    testApi = testRequestHandler()
    requestHandMgr.register(testApi)

    adApi = AdComposingApiRequestHandler()
    requestHandMgr.register(adApi)
