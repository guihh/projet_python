from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^load/$', views.chargement, name='chargement'),
    url(r'^get/(?P<gid>[0-9]+)/$', views.getLimite, name='getLimite'),
]
