from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # new url definition
    url(r'^home/$', views.contact, name='contact')]