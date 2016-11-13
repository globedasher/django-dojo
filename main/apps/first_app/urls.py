from django.conf.urls import url
#from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^house/(?P<track>[0-9])$', views.house),
]
