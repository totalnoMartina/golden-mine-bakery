""" Path module to render views through url patterns list """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mainapp'),
]
