from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Course
from ..authentication.models import User


def index(request):
    all_users = User.objects.all()
    try:
        courses = Course.objects.order_by('created_at')
        context = { 'courses': courses, 'all_users': all_users }
        return render(request, "courses_app/index.html", context)
    except:
        context = { 'all_users': all_users }
        return render(request, "courses_app/index.html", context)

def show(request):
    return render(request, 'courses_app/course.html', context)

def create(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_description = request.POST['course_description']
        user_id = request.session['id']
        user = User.objects.get(id=user_id)
        try:
            course = Course(course_name=course_name
                    ,course_description=course_description, user=user)
            course.save()
            return redirect(reverse('courses:index'))
        except:
            messages.error(request, "Error in values?")
            return redirect(reverse('courses:index'))
    else:
        messages.error(request, 'Method was not POST.')
        return redirect(reverse('courses:index'))

def delete(request, course_id):
    if request.method == 'GET':
        course = Course.objects.get(id=course_id)
        context = { 'course': course }
        return render(request, "courses_app/course.html", context)
    if request.method == 'POST':
        print('here!')
        Course.objects.filter(id=course_id).delete()
        return redirect(reverse('courses:index'))
    else:
        messages.error(request, 'Method was not POST or GET.')
        return redirect(reverse('courses:delete'))
