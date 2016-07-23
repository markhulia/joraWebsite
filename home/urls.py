from django.conf.urls import url
from . import views

# this is a namespace which is referenced to in .html files
# for example to load 'detail' page of home app, we will reference
# home:detail in our detail.html file
app_name = 'home'

urlpatterns = [
    # /home/
    url(r'^$', views.index, name='index'),

    # /home/<user.id>/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),

    # /home/<user.id>/favorite/
    url(r'^(?P<user_id>[0-9]+)/married/$', views.married, name='married'),
]
