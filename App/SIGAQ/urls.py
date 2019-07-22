# url.py file that has the URL configuration.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]