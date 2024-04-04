# user_management/urls.py
from django.urls import path
from . import views

# The given url runs the following function from view
urlpatterns = [
    path('', views.register_or_home, name='register_or_home'),
    path('register/', views.register_user, name='register'),
    path('home/', views.home, name='home'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/add_category/', views.add_category, name='add_category'),
    path('user/<int:user_id>/<int:category_id>/add_item', views.add_item, name='add_item'),
]
