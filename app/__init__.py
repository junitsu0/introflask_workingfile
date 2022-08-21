from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

# Create an instance of SQLAlchemy (the ORM) with the Flask Application
db = SQLAlchemy(app)
# Create an instance of Migrate which will be out migration engine and pass in the app and SQLAlchemy instance
migrate = Migrate(app, db)
# Create an instance of the LoginManager to handle authentication
login = LoginManager(app)


from . import routes, models

