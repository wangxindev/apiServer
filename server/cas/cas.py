from flask_cas import CAS


cas = CAS()

def setApp(app):
    cas.init_app(app=app)
    app.config['CAS_SERVER'] = 'https://cas.banggood.cn/cas/login'
    app.config['CAS_AFTER_LOGIN'] = 'route_root'

def getCAS():
    return cas