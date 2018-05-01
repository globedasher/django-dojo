from django.shortcuts import render
from . import models

# Create your views here.

def index(req):
    # 1
    #users = models.Users.objects.all()
    #friendships = models.Friendships.objects.filter(user__id=2)

    # 2
    #friendships = models.Friendships.objects.filter(user__first_name="Michael")
    
    # 3
    #friendships = models.Friendships.objects.exclude(user__first_name="Daniel")

    # 4
    friendships = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(user__last_name="Hernandez")

    # 5
    # .distinct() didn't work and provided the following error:
    # AssertionError at /
    # Cannot combine a unique query with a non-unique query.
    #$friendships = models.Friendships.objects.filter(user__id=1).order_by("friend__first_name") | models.Friendships.objects.filter(user__last_name="Hernandez")

    # 6
    #users = models.Users.objects.filter(usersfriend__friend__id=2)

    # 7
    #users = models.Users.objects.filter(friendsfriend__friend__id=2)

    #8
    users = models.Users.objects.filter(friendsfriend__user__id=1) | models.Users.objects.filter(friendsfriend__user__last_name="Hernandez")

    context = {'users':users, 'friendships': friendships}
    return render(req, "friendapp/index.html",context)
