from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from .models import Habit, Daily
from .forms import CreateUserForm, LoginForm, UserUpdateForm, ProfileUpdateForm, CreateHabitForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta, datetime
from collections import Counter


def home(request):
    context = {'user': request.user}
    return render(request, 'index.html', context=context)


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context=context)


def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")

    context = {"form": form}
    return render(request, "login.html", context=context)


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def dashboard(request):
    current_date = date.today()
    week = current_date.isocalendar()[1]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    start_current_week = current_date - timedelta(days=current_date.weekday())
    end_current_week = start_current_week + timedelta(days=6)

    week_dates = [{'day_of_week': days[i], 'date': start_current_week + timedelta(days=i)} for i in range(7)]
    habits = Habit.objects.filter(user=request.user)
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


@login_required(login_url="login")
def create_habit(request):
    form = CreateHabitForm()

    if request.method == "POST":
        form = CreateHabitForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            user_habit = Habit.objects.filter(user=request.user, title=title)
            if user_habit.exists():
                return HttpResponse(
                    status=204,
                    headers={
                        'HX-Trigger': json.dumps({
                            "HabitListChanged": None,
                            "showMessage": f"Sorry, the {title} is already in your list."
                        })
                    }
                )
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

    context = {"form": form}
    return render(request, "profile/create-habit.html", context=context)


@login_required(login_url="login")
def habits_list(request):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    current_user = request.user.id
    current_date = date.today()
    start_current_week = current_date - timedelta(days=current_date.weekday())

    week_dates = [{'day_of_week': days[i], 'date': start_current_week + timedelta(days=i)} for i in range(7)]
    habits = Habit.objects.filter(user=current_user)
    dailies = Daily.objects.all()

    context = {
        'dailies': dailies,
        'habits': habits,
        'days': days,
        'week_dates': week_dates,
    }
    return render(request, "profile/habits-list.html", context=context)


@login_required(login_url="login")
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

    context = {"form": form, "habit": habit}
    return render(request, "profile/edit-habit.html", context=context)


@login_required(login_url="login")
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
    return redirect("habits-list")


@login_required(login_url="login")
def user_profile(request):
    return render(request, "profile/user-profile.html")


@login_required(login_url="login")
def user_profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')

    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profile/user-profile-update.html', context)


@csrf_exempt
@login_required(login_url="login")
def mark_daily_done(request, daily_id):
    daily = get_object_or_404(Daily, id=daily_id)

    if request.method == "POST":
        daily.done = not daily.done
        daily.save()

        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "HabitListChanged": None,
                    "showMessage": f"Awesome! The {daily} updated."
                })
            }
        )

    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "HabitListChanged": None,
                "showMessage": "PROBLEM"
            })
        }
    )


@login_required(login_url="login")
def daily_list(request):
    dailies = Daily.objects.all()
    habits = Habit.objects.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    context = {"dailies": dailies, "habits": habits, "days": days}
    return render(request, "profile/daily-list.html", context=context)


@login_required(login_url="login")
def view_habits(request):
    habits = Habit.objects.filter(user=request.user)

    context = {"habits": habits}
    return render(request, "profile/view-habits.html", context=context)


@login_required(login_url="login")
def view_dailies(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    dailies = Daily.objects.filter(habit=habit, habit__user=request.user)

    context = {"habit": habit, "dailies": dailies}
    return render(request, "profile/view-dailies.html", context=context)


@login_required(login_url="login")
def statistics(request):
    selected_date = request.GET.get('date')
    parsed_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
    dailies = Daily.objects.filter(date=parsed_date, habit__user=request.user)
    habits = Habit.objects.filter(user=request.user)
    total_dailies = dailies.count()
    completed_dailies = dailies.filter(done=True).count()
    remained = total_dailies - completed_dailies
    completion_rate = f"{round((completed_dailies / total_dailies) * 100 if total_dailies > 0 else 0)}%"

    categories = [habit.category for habit in habits]
    category_counts = Counter(categories)
    category_counts_values = list(category_counts.values())

    context = {
        'habits': habits,
        'dailies': dailies,
        'total_dailies': total_dailies,
        'category_counts': category_counts,
        'category_counts_values': category_counts_values,
        'remained': remained,
        'completion_rate': completion_rate,
        'selected_date': selected_date,
    }
    return render(request, "profile/statistics.html", context=context)



def view_habits_cards(request):
    habits = Habit.objects.filter(user=request.user)

    context = {"habits": habits}
    return render(request, "profile/view-habits-cards.html", context=context)
