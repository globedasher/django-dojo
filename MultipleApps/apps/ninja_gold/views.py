from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime
import random

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'action' in request.session:
        request.session['action'] = {}
    places = {
            "Farm": [10, 20],
            "Cave": [5, 10],
            "House": [2, 5],
            "Casino": [-50, 50],
            }
    context = { 'places': places }
    return render(request, 'ninja_gold/index.html', context)

def process(request, location):
    if request.method == "GET":
        return redirect(index)
    # The upper bound has to be one above the max
    values = {
            "Farm": [10, 21],
            "Cave": [5, 11],
            "House": [2, 6],
            "Casino": [-50, 51],
            }
    #print(values[location])
    #print(type(values[location]))
    earned = random.randrange(values[location][0], values[location][1])
    request.session['gold'] += earned
    string = "Earned {} gold from the {}! @ {}" .format(
            earned, location, datetime.now())
    request.session['action'] = string
    #print(request.session['action'])
    return redirect(reverse('gold:index'))

def reset(request):
    request.session['gold'] = 0
    request.session['action'] = ''
    return redirect(reverse('gold:index'))

def wrong(request):
    return HttpResponse("Wrong!")
