from app.api.domain.course.services.course_service import CourseService
from app.api.domain.course.entities.course import Course
from app.api.helpers.api import Api


class CourseController(Api):
    def get_list(self):
        course_service = CourseService.get_instance()
        course_collection = []

        course: Course
        for course in course_service.get_paginated_items():
            course_collection.append({
                'id': course.get_id(),
                'name': course.get_name(),
                'is_active': course.isActive()
            })

        return self.compose_data(course_collection)
