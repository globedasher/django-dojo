from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/$', views.create),
    url(r'^delete/(?P<course_id>[0-9]+)/$', views.delete),
]
