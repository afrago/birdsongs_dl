import os

app_dir = os.path.abspath(os.path.dirname(__file__))



class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### Flask-Mail configurations #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'anderfrago@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    ALLOWED_EXTENSIONS = set(['mp3', 'mp4'])
    UPLOAD_FOLDER = './deeplearning/demo/data/audio_samples/'

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in BaseConfig.ALLOWED_EXTENSIONS

class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
                              'mysql+pymysql://root:pass@localhost/flask_app_db'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
                              'mysql+pymysql://root:pass@localhost/flask_app_db'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
                              'mysql+pymysql://root:pass@localhost/flask_app_db'