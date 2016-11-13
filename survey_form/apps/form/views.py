from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if 'id' not in request.session:
        request.session['id'] = 0
    if 'name' not in request.session:
        request.session['name'] = ""
    if 'location' not in request.session:
        request.session['location'] = ""
    if 'language' not in request.session:
        request.session['language'] = ""
    if 'comment' not in request.session:
        request.session['comment'] = ""
    return render(request, "form/index.html")

def surveys_process(request):
    #print("*"*50)
    #print(request.POST)
    #print("*"*50)
    request.session['id'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect(result)

def result(request):
    return render(request, "form/result.html")
