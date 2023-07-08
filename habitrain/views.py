from django.shortcuts import render, redirect
from .models import Habit, Daily, Profile, User
from .forms import (
    CreateUserForm,
    LoginForm,
    UserUpdateForm,
    ProfileUpdateForm,
    CreateHabitForm,
    CreateDailyForm,
)
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta




def home(request):
    return render(request, 'index.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {
        "form": form
    }

    return render(request, "register.html", context=context)


def login(request):
    form = LoginForm

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    context = {
        "form": form
    }

    return render(request, "login.html", context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("")


@login_required(login_url="login")
def dashboard(request):
    current_date = date.today()
    week = current_date.isocalendar()[1]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    start_current_week = current_date - timedelta(days=current_date.weekday())
    end_current_week = start_current_week + timedelta(days=6)

    week_dates = []
    for i in range(7):
        day = start_current_week + timedelta(days=i)
        week_dates.append({'day_of_week': days[i], 'date': day})
    habits = Habit.objects.all()
    dailies = Daily.objects.all()

    context = {
        "week": week,
        'week_dates': week_dates,
        "current_date": current_date,
        'habits': habits,
        'dailies': dailies,
        'days': days,
    }
    return render(request, "profile/dashboard.html", context)