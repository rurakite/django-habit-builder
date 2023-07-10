from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-habit', views.create_habit, name="create-habit"),
    path('habits-list', views.habits_list, name="habits-list"),
    path('edit-habit/<str:pk>', views.edit_habit, name="edit-habit"),
    path('delete-habit/<str:pk>', views.delete_habit, name="delete-habit"),path('user-profile', views.user_profile, name="user-profile"),
    path('user-profile-update', views.user_profile_update, name="user-profile-update"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('daily/<str:daily_id>', views.mark_daily_done, name='mark_daily_done'),
    path('daily-list', views.daily_list, name="daily-list"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)