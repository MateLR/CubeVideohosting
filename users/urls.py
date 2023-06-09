from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registation/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('customer/<int:pk>/', views.customer, name='customer')
]
