from django.conf.urls import url

from . import views

app_name = 'time'
urlpatterns = [
    url(r'^time$', views.index, name="index"),
]
