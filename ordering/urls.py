from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_order, name='view_order'),
] 
