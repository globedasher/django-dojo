from __future__ import unicode_literals

from django.db import models

from ..authentication.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=60)
    course_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
