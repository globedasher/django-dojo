from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class EmailManager(models.Manager):
    def register(self, email_address):
        print(email_address)
        #print("Register email route")
        if not EMAIL_REGEX.match(email_address):
            #print("email failed!")
            return (False, "Error")
        else:
            #print("good!")
            email = Email(email_address=email_address, created_at=datetime.now(), updated_at=datetime.now())
            print(email.__dict__)
            email.save()
            return (True, email)

class Email(models.Model):
    email_address = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmailManager()
