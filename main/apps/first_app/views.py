from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    #print("index")
    response = "Hello, I am a your index request."
    return render(request, 'first_app/index.html')

def users(request):
    #print("users")
    response = "Hello, I am a your show request."
    context = { 'time_of_day': datetime.now() }
    return render(request, 'first_app/users.html', context)
