# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_or_home, name='register_or_home'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),
    path('user/<int:user_id>/', views.kits_detail, name='kits_detail'),
    path('user/<int:user_id>/add_category/', views.add_category, name='add_category'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
]
