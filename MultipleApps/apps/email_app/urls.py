from django.conf.urls import url

from . import views

app_name = 'email_validation'
urlpatterns = [
    url(r'^email_validation$', views.index, name='index'),
    url(r'^email_validation/submit$', views.submit, name='submit'),
]
