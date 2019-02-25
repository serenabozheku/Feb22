from flask import Blueprint

item = Blueprint('item', __name__, template_folder='templates')

@item.route('/')

def show():
    return'I am Blueprint'