from __future__ import unicode_literals

from django.db import models

from ..authentication.models import User


class CourseManager(models.Manager):
    def add_user_to_course(self, user_id, course_id):
        course = self.get(id=course_id)
        user = User.objects.get(id=user_id)
        course.student.add(user)
        course.save()
        return (True, course)
            

class Course(models.Model):
    course_name = models.CharField(max_length=60)
    course_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
    student = models.ManyToManyField('authentication.User', related_name="courses")
