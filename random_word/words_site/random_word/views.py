from django.shortcuts import render, redirect
import string
import random

# Create your views here.

def index(request):
    # When the index is first reached, if the request.session['attempt'] and
    # request.session['random_word'] do not exist, create those variables.
    if not request.session['attempt']:
        request.session['attempt'] = 0
    if not request.session['random_word']:
        request.session['random_word'] = ""
    return render(request, 'random_word/index.html')

def generate(request):
    # When the generate route is run, increase the attempt count, reset the
    # random word, generate the random word, then redirect to the index to
    # display the random word.
    request.session['attempt'] += 1
    request.session['random_word'] = ""
    size = 14
    choice = [random.choice(string.ascii_uppercase
                + string.digits) for _ in range(size)]
    for element in choice:
        request.session['random_word'] += element
    return redirect(index)

def clear(request):
    # When the clear route is run, clear the attempt and random_word variables.
    request.session['attempt'] = 0
    request.session['random_word'] = ""
    return redirect(index)
