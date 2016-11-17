from django.shortcuts import render, redirect, HttpResponse
import bcrypt

from .models import User

# Create your views here.

def index(request):
    user = User.objects.login("globe.dasher@gmail.com", "time")
    return render(request, 'log_n_reg_app/index.html')
