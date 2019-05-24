from flask import Flask
from flask_script import Manager
import os, config
from app.main import main

# create application instance
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
app.register_blueprint(main)

# import views
from . import views

