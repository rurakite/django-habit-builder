from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create-habit/', views.create_habit, name="create-habit"),
    path('habits-list/', views.habits_list, name="habits-list"),
    path('view-habits/', views.view_habits, name="view-habits"),
    path('view-dailies/<int:habit_id>/', views.view_dailies, name="view-dailies"),
    path('edit-habit/<str:pk>/', views.edit_habit, name="edit-habit"),
    path('delete-habit/<str:pk>/', views.delete_habit, name="delete-habit"),
    path('user-profile/', views.user_profile, name="user-profile"),
    path('user-profile-update/', views.user_profile_update, name="user-profile-update"),
    path('daily/<str:daily_id>/', views.mark_daily_done, name='mark-daily-done'),
    path('daily-list/', views.daily_list, name="daily-list"),
    path('statistics/', views.statistics, name="statistics"),
    path('view-habits-cards/', views.view_habits_cards, name="view-habits-cards"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)