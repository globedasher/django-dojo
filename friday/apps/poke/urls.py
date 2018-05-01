from django.conf.urls import url

from . import views

app_name = 'poke'
urlpatterns  = [
    url(r'^poke/$', views.index, name = "index"),
    url(r'^poke/new/(?P<user_id>[0-9]+)/$', views.new, name = "new"),
]
