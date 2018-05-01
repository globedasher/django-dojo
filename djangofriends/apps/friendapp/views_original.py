from django.shortcuts import render
from . import models

# Create your views here.

def index(req):
    #users = models.Users.objects.all()

    # 1
    #users = models.Users.objects.filter(last_name="Rodriguez")
    
    # 2
    #users = models.Users.objects.exclude(last_name="Rodriguez")

    # 3
    #users = models.Users.objects.filter(last_name="Rodriguez") | models.Users.objects.filter(first_name="Daniel")

    # 4
    #users = models.Users.objects.filter(last_name="Rodriguez").exclude( first_name="Madison")

    # 5
    #users = models.Users.objects.all().exclude(first_name='Daniel').exclude(first_name="Michael")

    # 6
    # So... I got an error that this object did not have a query. After
    # removing the query line, the users object prints it is an object called
    # Users. This appears to be made from the Users class in models.py
     
    # Once I created the line below, I had to use {{ users.first_name }} {{
    # users.last_name }} to print the user first and last name in index.html

    #users = models.Users.objects.get(id=1)
    
    # 7
    # This error returns stating the get() returned three items instead of
    # one... Based on this, I would assume the get function expects only one
    # row to be returned. I also had to remove the users for loop to get the
    # singular user object above to display.

    #users = models.Users.objects.get(last_name="Rodriguez")

    # 8
    # Users matching query does not exist.
    #users = models.Users.objects.get(id=10000)

    # 9
    #users = models.Users.objects.order_by('first_name')

    # 10
    users = models.Users.objects.order_by('last_name').reverse()

    # 11
    friendships= models.Friendships.objects.all()
    #print(friendships)

    # 12
    #f = models.Friendships.objects.filter(user=4)

    # 13
    #f = models.Friendships.objects.filter(friend=4)

    # 14
    f = models.Friendships.objects.exclude(user=4).exclude(user=5).exclude(user=6)

    context = {'users':users, 'friendships':f}
    return render(req, "friendapp/index.html",context)
