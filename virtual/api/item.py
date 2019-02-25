from flask import Blueprint

item = Blueprint('item', __name__, template_folder='template')

@item.route('/')
def show():
    return'I am Blueprint'