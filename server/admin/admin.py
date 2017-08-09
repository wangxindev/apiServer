
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_cas import login_required
from server.cas.cas import getCAS

import os.path as op

class MyView(BaseView):

    #这里类似于app.route()，处理url请求
    @expose('/')
    @login_required
    def index(self):
        print('==========' * 4)
        username = getCAS().username,
        print(username)
        display_name = getCAS().attributes['cas:displayName']
        print(display_name)
        print('==========' * 4)

        return self.render('index.html')

class UserView(ModelView):

    #这三个变量定义管理员是否可以增删改，默认为True
    can_delete = False
    can_edit = True
    can_create = True

    #这里是为了自定义显示的column名字
    def __init__(self, User, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UserView, self).__init__(User, session, **kwargs)

    column_labels = dict(
        username='name',
        # id='id',
        mail='email'
    )



class ApiServerAdmin(object):
    def __init__(self, app, dbMgr):

        self.__app = app
        self.__db = app.extensions['sqlalchemy'].db
        self.__admin = Admin(app,template_mode='bootstrap3')
        # self.__admin.add_view(MyView('my view'))
        self.__admin.add_view(UserView(dbMgr.User,self.__db.session))
        path = op.join(op.dirname(__file__), 'static')
        self.__admin.add_view(FileAdmin(path, '/static/', name='Static Files'))


