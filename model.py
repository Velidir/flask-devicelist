from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)  
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)



class devicelist(db.Model):
    country = db.Column(db.Text)
    project = db.Column(db.Text)
    ip = db.Column(db.Text,primary_key=True)
    type = db.Column(db.Text)
    access = db.Column(db.Text)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    enable = db.Column(db.Text)
    backedup = db.Column(db.Text)
    description = db.Column(db.Text)
    dmvpn = db.Column(db.Text)
    
