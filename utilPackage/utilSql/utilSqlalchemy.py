from flask_sqlalchemy import SQLAlchemy

from app.app import getAppMgr

db = SQLAlchemy(None)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.username = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class sqlAlchemyDB(object):
    @staticmethod
    def sqlDB_init():
        app = getAppMgr().get('flaskApp')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Volumes/work/3.code/APIServer/tmp/test.db'
        db.init_app(app)

    @staticmethod
    def getDB():
        return db

getAppMgr().insert('User',User)
getAppMgr().insert('sqlAlchemyDB', sqlAlchemyDB)


'''
例子
db.create_all()
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
User.query.all()
User.query.filter_by(username='admin').first()
'''



