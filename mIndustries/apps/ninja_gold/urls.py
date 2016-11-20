from django.conf.urls import url

from . import views

app_name = 'gold'
urlpatterns = [
    url(r'^gold$', views.index, name="index"),
    # the below name change to the named route may need some changes to process
    # the locations as I have it currently.
    url(r'^gold/process_money/(?P<location>\w+)', views.process, name="process"),
    url(r'^gold/reset$', views.reset, name="reset"),
]
