from flask import Blueprint
from app.api.controllers.course import CourseController

course_route = Blueprint('course', __name__, url_prefix='/course/')


@course_route.get('/get-list')
def getList():
    course_controller = CourseController()
    return course_controller.get_list()
