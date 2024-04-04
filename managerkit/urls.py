# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_or_home, name='register_or_home'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]
