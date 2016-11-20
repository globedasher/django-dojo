from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HobbyManager(models.Manager):
    def ValidateCreation(self, **kwargs):
        if not kwargs['name']:
            print("error")
        pass

class Hobby(models.Model):
    name = models.CharField(max_length=200)
    person = models.ManyToManyField(User)
    category = models.CharField(max_length=200)
    danger_level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = HobbyManager()
    
