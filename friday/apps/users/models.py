from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]')

# Create your models here.

class UserManager(models.Manager):

    def login(self, email, password):
        errors = []

        # password validations
        if not password:
            errors.append("Please enter a password.")

        if not errors:
            # Get the user object and check the password (hashed through
            # bcrypt)
            try:
                user = User.objects.get(email=email)
                encoded_hash = user.pw_hash.encode('utf-8')
                encoded_pw = password.encode('utf-8')
                if bcrypt.hashpw(encoded_pw, encoded_hash) == encoded_hash:
                    return (True, user)
                else:
                    errors.append("Error.")
                    return (False, errors)
            except:
                errors.append("Error.")
                return(False, errors)
        else:
            return (False, errors)
                

    def register(self, *args):
        name = args[0]['name']
        alias = args[0]['alias']
        birthday = args[0]['birthday']
        password = args[0]['password']
        password2 = args[0]['password2']
        email = args[0]['email']

        print(unicode(str(datetime.date(datetime.now())), 'utf-8'))

        errors = []
        # Build validations here

        # name validations
        if not name:
            errors.append("Name must exist.")
        elif not name.istitle():
            errors.append("""Name Must Be Written It Title Case.  <-- this is an example""")
        elif len(name) < 2:
            errors.append("Name must be longer than two characters.")

        # alias validations
        if not alias:
            errors.append("Alias must exist.")
        elif not alias.isalnum():
            # Sorry, I made a personal executive decision that I would not go
            # with special characters allowed in the aliases. Alphanumeric
            # only.
            errors.append("Alias must contain letters and numbers only.")
        elif len(alias) < 2:
            errors.append("Alias must be longer than two characters.")

        # email validations
        if not email:
            errors.append("Please enter an email address.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email address.")

        # password validations
        if not password or not password2:
            errors.append("Please enter a password and confirmation.")
        if not password == password2:
            errors.append("Passwords do not match.")
        if not len(password) >= 8:
            errors.append("Password must be at least 8 characters long.")
        if not password.isalnum():
            errors.append("Password must be alphanumeric.")
        # decimal 33 to 126 seems to encompass all special symbols.
            for letter in password:
                print(letter)
        elif not PASSWORD_REGEX.match(password):
            errors.append("Password must include one capital and one number")

        # birthday validations
        if not birthday:
            errors.append("Please add your birthday!")
        elif birthday > unicode(str(datetime.date(datetime.now())), 'utf-8'):
            errors.append("Birthday cannot be in the future.")


        # if no errors exist in the validation, the user can be registered!
        if not errors:
            encoded_pw = password.encode('utf-8')
            pw_hash = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
            user = User(name=name, alias=alias, pw_hash=pw_hash, email=email, birthday=birthday) 
            user.save()
            return (True, user)
        # OTHERWISE! We will return to the index page and print all the errors
        # that have been appended to the errrors list we are passing below.
        else:
            return (False, errors)


class User(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    birthday = models.DateField()
    pw_hash = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
