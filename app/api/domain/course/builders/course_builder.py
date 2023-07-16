from app.api.domain.course.entities.course import Course


class CourseBuilder:
    def __init__(self):
        self.course = Course.get_instance()

    @classmethod
    def get_instance(cls):
        return cls()

    def get_paginated_items(self):
        return self.course.query.paginate()
