from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_order, name='view_order'),
    path('add/<item_id>/', views.add_an_order, name='add_an_order'),
    path('adjust/<item_id>/', views.adjust_order, name='adjust_order'),
    path('remove/<item_id>/', views.remove_from_order, name='remove_from_order'),
] 
