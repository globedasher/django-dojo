from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.none),
    url(r'^ninjas/(?P<color>\w+)$', views.index),
    url(r'^ninjas/$', views.index),
    url(r'^.', views.wrong),
]
