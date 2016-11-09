from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    dictionary = { 'time': datetime.now()}
    return render(request, 'timedisplay/index.html', dictionary)
