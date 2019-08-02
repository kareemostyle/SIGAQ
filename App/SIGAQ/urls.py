# url.py file that has the URL configuration.
from django.urls import path
from . import views

app_name = 'SIGAQ'
urlpatterns = [
    path('', views.index, name='index'),
]