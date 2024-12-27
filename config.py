import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY              = os.environ.get('SECRET_KEY') or 'afs$$12'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    MAIL_SERVER             = os.environ.get('MAIL_SERVER')
    MAIL_PORT               = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS            = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME           = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD           = os.environ.get('MAIL_PASSWORD')

    APP_NAME                = os.environ.get('APP_NAME')
    ADMINS                  = os.environ.get('ADMINS').split(",")