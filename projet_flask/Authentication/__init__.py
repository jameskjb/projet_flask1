from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from urllib.parse import quote_plus
from flask_login import LoginManager


app = Flask(__name__)




app.config['SECRET_KEY'] = '25d25644aa4b66be072ce667be8586ad'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# from .models import User
@login_manager.user_loader
def  load_user(user_id):
      return User.query,get(int(user_id))

from Authentication import routes  