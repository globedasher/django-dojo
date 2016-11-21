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
    courses = Course.objects.all()
    users = User.objects.all()
    course_filter = Course.objects.filter()
    for course in course_filter:
        print(course.student)
    context = { 'courses': courses, 'users': users, 'course_filter': course_filter }
    return render(request, 'courses_app/user_course.html', context)


def create(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        course_description = request.POST['course_description']
        try:
            course = Course(course_name=course_name
                    ,course_description=course_description)
            course.save()
            return redirect(reverse('courses:index'))
        except:
            messages.error(request, "Error in values?")
            return redirect(reverse('courses:index'))
    else:
        messages.error(request, 'Method was not POST.')
        return redirect(reverse('courses:index'))


# The following is used to assign existing users to exsiting courses.
def assign(request):
    if request.method == 'POST':
        # request.POST returns the course and user id to link in the Assigned
        # table.
        user_id = request.POST['users']
        course_id = request.POST['courses']
        tuple_return = Course.objects.add_user_to_course(user_id=user_id
                , course_id=course_id)
        messages.success(request, "You have added a user to a course.")
        return redirect(reverse('courses:show'))
    else:
        messages.error(request, 'Method was not POST.')
        return redirect(reverse('course:show'))


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
