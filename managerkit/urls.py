# user_management/urls.py
from django.urls import path
from . import views

# The given url runs the following function from view
urlpatterns = [
    path('', views.register_or_home, name='register_or_home'),
    path('home/', views.home, name='home'), # everyone's kit
    path('register/', views.register_user, name='register'),

    path('kit/<int:user_id>/', views.kits_detail, name='kits_detail'), # one person's kit
    path('manage_users/', views.manage_users, name='manage_users'),
    path('notifications/', views.notifications, name='notifications'),
    path('setting/', views.setting, name='settings'),

    path('manage_users/user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/add_category/', views.add_category, name='add_category'),
    path('user/<int:user_id>/<int:category_id>', views.delete_category, name='delete_category'),
    path('user/<int:user_id>/<int:category_id>/add_item', views.add_item, name='add_item'),
    path('user/<int:user_id>/<int:category_id>/<int:item_id>', views.delete_item, name='delete_item'),

    path('manage_users/user/<int:user_id>/edit_user_detail', views.edit_user_detail, name='edit_user_detail'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'), # Usage of URL to run function
    path('update_user/<int:user_id>/', views.update_user, name='update_user'), # Usage of URL to run function
    path('user/<int:user_id>/recommendations/', views.recommendations, name='recommendations'),
]
