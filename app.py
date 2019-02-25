from flask import Flask
from ext import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True

db.init_app(app)


@app.before_first_request
def create():
    db.create_all()