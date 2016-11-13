from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def none(request):
    return HttpResponse("No ninjas here.")

def index(request, color = ''):
    colors = "blue", "red", "orange", "purple"
    context = { 'color': color }
    # If the color passed in the url matches one of the four in the colors
    # list, add that color to the context dictionary and pass that to the
    # template for rendering. 
    if color in colors:
        # (The index.html template has if statements to display the individual
        # turtles.)
        return render(request, "disappearing_ninjas/index.html", context)
    # If there is no color passed, in the case of /ninjas/, the colors variable
    # will be a blank string and all turtles in the template will be rendered.
    if color == '':
        return render(request, "disappearing_ninjas/index.html", context)

def wrong(request):
    return render(request, "disappearing_ninjas/404.html")
