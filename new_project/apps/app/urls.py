from django.urls.conf import url, HttpResponse
#from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', url(views.index)),
]
