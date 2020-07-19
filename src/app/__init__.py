from flask import Flask
from app.settings import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_image_alchemy.storages import FileStorage

app = Flask(__name__)
app.config.from_object(Config)
storage = FileStorage()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import views, models