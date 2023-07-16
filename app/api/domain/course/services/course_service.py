from app.api.domain.course.builders.course_builder import CourseBuilder


class CourseService:
    def __init__(self):
        self.course_builder = CourseBuilder.get_instance()

    @classmethod
    def get_instance(cls):
        return cls()

    def get_paginated_items(self):
        return self.course_builder.get_paginated_items()
