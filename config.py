from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bidit:bidit@ec2-54-213-102-70.us-west-2.compute.amazonaws.com/bidit'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db = db)