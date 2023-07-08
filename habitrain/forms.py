from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from django.forms import ModelForm
from .models import Habit, Daily, Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateHabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ["title", "description", "category", "start_date", "end_date", ]
        exclude = ["user", ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateDailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['date', 'habit', 'done', ]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'occupation', "location", "profile_image", ]
