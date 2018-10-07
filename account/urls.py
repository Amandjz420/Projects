from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^account/$', views.index, name='index'),
]