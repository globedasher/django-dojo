from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):

    def login(self, email, password):
        print("Running Login function")
        print ("Running a login function!")
        print ("If successful login occurs, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }")
        return (True, user)

    def register(self, **kwargs):
        print("Running Register function")
        print ("Register a user here")
        print ("If successful, maybe return {'theuser':user} where user is a user object?")
        print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
        for item in kwargs:
            print(item)
        return ("This is my return statement from register.")


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    pw_hash = models.CharField(max_length=256)
    objects = UserManager()
