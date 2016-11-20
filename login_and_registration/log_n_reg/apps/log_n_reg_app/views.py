from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
import bcrypt

from .models import User

# Create your views here.

def index(request):
    all_users = User.objects.all()
    context = { 'all_users': all_users }
    return render(request, 'log_n_reg_app/index.html', context)

""" 
The tuple_return in the login and register functions return a true if the email
is cleared by regex match and and User object. If the email is not cleared by
regex, the tuple comes back as false at [0] and an error message at [1].
"""

def login(request):
    if request.method == 'POST':
        tuple_return = User.objects.login(request.POST['email'], 
                request.POST['password'])
        # tuple_return[0] is false if email didn't pass regex
        if tuple_return[0] == False:
            messages.error(request, "Login errors:")
            # Here, tuple_retun[1] is a list of error messages to flash to user
            for item in tuple_return[1]:
                messages.error(request, item)
            return redirect(reverse('index'))
        # tuple_return[0] is false if email didn't pass regex
        elif tuple_return[0] == True:
            all_users = User.objects.all()
            context = { 'user': tuple_return[1], 'all_users': all_users }
            messages.success(request, "Success!")
            return render(request, "log_n_reg_app/success.html", context)
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        tuple_return = User.objects.register(request.POST)
        # tuple_return[0] is false if email didn't pass regex
        if tuple_return[0] == False:
            messages.error(request, "Registration errors:")
            # Here, tuple_retun[1] is a list of error messages to flash to user
            for item in tuple_return[1]:
                messages.error(request, item)
            return redirect(reverse('index'))
        # tuple_return[0] is false if email didn't pass regex
        elif tuple_return[0] == True:
            all_users = User.objects.all()
            context = { 'user': tuple_return[1], 'all_users': all_users }
            messages.success(request, "Successful registration!")
            return render(request, "log_n_reg_app/success.html", context)
    else:
        messages.error(request, "Incorrect Http request.")
        return redirect(reverse('index'))
