from django.shortcuts import render
from django.utils import timezone
import pytz

# Create your views here.

def index(request):
    dictionary = { 'time': timezone.now()}
    return render(request, 'timedisplay/index.html', dictionary)
