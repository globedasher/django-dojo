from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^courses$', views.index, name="index"),
    url(r'^courses/create$', views.create, name="create"),
    url(r'^courses/show$', views.show, name="show"),
    url(r'^courses/assign$', views.assign, name="assign"),
    url(r'^courses/delete/(?P<course_id>[0-9]+)/$', views.delete, name="delete"),
]
