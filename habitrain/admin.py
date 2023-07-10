from django.contrib import admin
from .models import Habit, Daily

admin.site.site_header = 'HabiTrain Dashboard'


admin.site.register(Habit)
admin.site.register(Daily)