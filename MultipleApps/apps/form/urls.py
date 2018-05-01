from django.conf.urls import url

from . import views

app_name = 'form'
urlpatterns = [
    url(r'^form$', views.index, name="index"),
    url(r'^form/surveys/process$', views.surveys_process, name="process"),
    url(r'^form/result$', views.result, name="result"),
]
