from django.conf.urls import url

from . import views

app_name = 'books'
urlpatterns  = [
    url(r'^books$', views.index, name = "index"),
    url(r'^books/new$', views.new, name = "new"),
    url(r'^books/create$', views.create, name = "create"),
    url(r'^books/(?P<book_id>[0-9]+)/$', views.show, name = "show"),
    url(r'^books/(?P<book_id>[0-9]+)/review$', views.review, name = "review"),
]

