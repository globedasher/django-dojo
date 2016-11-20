from django.shortcuts import render, redirect, HttpResponse, messages

# Create your views here.

def index(request):
    return HttpResponse("You are here.")
