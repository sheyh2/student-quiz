from flask import Flask, Blueprint
from app.api.routes.course import course_route


class BaseRoutes:
    def __init__(self, app: Flask):
        self.app = app

    def init_routes(self):
        api = Blueprint('api', __name__, url_prefix='/api/')

        api.register_blueprint(course_route)

        self.app.register_blueprint(api)
