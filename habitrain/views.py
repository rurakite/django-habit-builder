from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
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


@login_required(login_url="my-login")
def create_habit(request):
    form = CreateHabitForm()

    if request.method == "POST":
        form = CreateHabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "HabitListChanged": None,
                        "showMessage": f"Great! The {habit.title} added."
                    })
                }
            )

    context = {
        "form": form
    }
    return render(request, "profile/create-habit.html", context=context)


@login_required(login_url="my-login")
def habits_list(request):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    current_date = date.today()
    start_current_week = current_date - timedelta(days=current_date.weekday())

    week_dates = []
    for i in range(7):
        day = start_current_week + timedelta(days=i)
        week_dates.append({'day_of_week': days[i], 'date': day})

    habits = Habit.objects.all()
    dailies = Daily.objects.all()


    context = {
        'dailies': dailies,
        'habits': habits,
        'days': days,
        'week_dates': week_dates,

    }
    return render(request, "profile/habits-list.html", context=context)


@login_required(login_url="my-login")
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    form = CreateHabitForm(instance=habit)
    if request.method == "POST":
        form = CreateHabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "HabitListChanged": None,
                        "showMessage": f"Awesome! The {habit.title} updated."
                    })
                }
            )

    context = {
        "form": form,
        "habit": habit
    }
    return render(request, "profile/edit-habit.html", context=context)


@login_required(login_url="my-login")
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habit.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "HabitListChanged": None,
                    "showMessage": f"The {habit.title} deleted."
                })
            }
        )



def user_logout(request):
    auth.logout(request)

    return redirect("")


@login_required(login_url="my-login")
def user_profile(request):
    return render(request, "profile/user-profile.html")