from django.shortcuts import render, HttpResponse

from .models import user

# Create your views here.

def index(request):
    return HttpResponse("You made it again!")
