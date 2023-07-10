from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-habit', views.create_habit, name="create-habit"),
    path('habits-list', views.habits_list, name="habits-list"),
    path('edit-habit/<str:pk>', views.edit_habit, name="edit-habit"),
    path('delete-habit/<str:pk>', views.delete_habit, name="delete-habit"),
    
]