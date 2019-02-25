from flask import Blueprint, render_template

course = Blueprint('course', __name__, template_folder='templates')


courses = ['INF310', 'ECO400','ECO311']

@course.route('/')

def course_list():
    return render_template('index.html', courses = course_list)