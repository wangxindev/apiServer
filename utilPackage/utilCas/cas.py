from flask_cas import CAS
from app.app import getAppMgr


class mycas(object):
    @staticmethod
    def cas_init():
        cas = CAS()
        app = getAppMgr().get('flaskApp')
        cas.init_app(app=app)
        app.config['CAS_SERVER'] = 'https://cas.banggood.cn/cas/login'
        app.config['CAS_AFTER_LOGIN'] = 'route_root'
        getAppMgr().insert('cas', cas)

getAppMgr().insert('mycas', mycas)


