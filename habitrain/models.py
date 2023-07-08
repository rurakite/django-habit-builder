from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(default='avatar.jpg', upload_to='profile_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Habit(models.Model):

    CATEGORIES = [
        ('HEALTH', 'HEALTH'),
        ('FITNESS', 'FITNESS'),
        ('LEARNING', 'LEARNING'),
        ('DESTRUCTIVE', 'DESTRUCTIVE'),
        ('PRODUCTIVITY', 'PRODUCTIVITY'),
        ('SELF-CARE', 'SELF-CARE'),
        ('FINANCE', 'FINANCE'),
        ('RELATIONSHIP', 'RELATIONSHIP'),
        ('MINDFULNESS', 'MINDFULNESS'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    category = models.CharField(choices=CATEGORIES, max_length=20, default=None)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=None)

    def __str__(self):
        return self.title


class Daily(models.Model):
    date = models.DateField()
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, default=None)
    done = models.BooleanField(default=False)

    class Meta:
        unique_together = ['habit', 'date']

    def __str__(self):
        return f'Daily record for {self.habit} - {self.date}'
