from django.shortcuts import render
from .models import Habit, Daily, Profile, User
from .forms import (
    CreateUserForm,
    LoginForm,
    UserUpdateForm,
    ProfileUpdateForm,
    CreateHabitForm,
    CreateDailyForm,
)




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