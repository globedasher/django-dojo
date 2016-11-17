from django.shortcuts import render, redirect, HttpResponse
# Import the messages (flash) system
from django.contrib import messages

from .models import Course, User

# Create your views here.

def index(request):
    print("Running Index method. Calling out to user.")
    user = User.objects.login('rm@gmail.com')
    print(user)
    #print(type(user))
    #if 'error' in user:
    #    pass
    #if 'theuser' in user:
    #    pass
    #return HttpResponse("Done.")


    courses = Course.objects.order_by('created_at')
    context = { 'courses': courses }
    return render(request, "courses_app/index.html", context)

def create(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_description = request.POST['course_description']
        #print(course_name)
        #print(course_description)
        course = Course(course_name=course_name, course_description=course_description)
        course.save()
        return redirect(index)
    else:
        messages.error(request, 'Method was not POST.')
        return redirect(index)

def delete(request, course_id):
    if request.method == 'GET':
        course = Course.objects.get(id=course_id)
        context = { 'course': course }
        return render(request, "courses_app/course.html", context)
    if request.method == 'POST':
        Course.objects.filter(id=course_id).delete()
        return redirect(index)
    else:
        messages.error(request, 'Method was not POST or GET.')
        return redirect(delete)
