from __future__ import unicode_literals

from django.db import models
from ..users.models import User

class Poke(models.Model):
    # This is the person being poked.
    poked = models.ForeignKey(User, related_name="other_user")

    # This is the logged in user doing the poking.
    pointy_end = models.ForeignKey(User, related_name="user")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
