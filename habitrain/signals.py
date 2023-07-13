from django.contrib.auth.models import User
from .models import Profile, Habit, Daily
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import timedelta


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Habit)
def create_or_update_daily_records(sender, instance, created, **kwargs):
    if created:
        create_daily_records(instance)
    else:
        update_daily_records(instance)

def create_daily_records(habit):
    start_date = habit.start_date
    end_date = habit.end_date

    # Calculate the number of days between the start and end dates
    num_days = (end_date - start_date).days + 1

    # Generate Daily instances for each date within the range
    daily_records = [
        Daily(date=start_date + timedelta(days=i), habit=habit)
        for i in range(num_days)
    ]

    # Bulk create the Daily instances to minimize database queries
    Daily.objects.bulk_create(daily_records)

def update_daily_records(habit):
    # Retrieve the existing Daily instances associated with the habit
    daily_records = habit.daily_set.all()

    # Calculate the number of days between the updated start and end dates
    num_days = (habit.end_date - habit.start_date).days + 1

    # Check if the number of days has changed
    if num_days != daily_records.count():
        # Generate new Daily instances for the added days
        new_daily_records = [
            Daily(date=habit.start_date + timedelta(days=i), habit=habit)
            for i in range(num_days)
            if not daily_records.filter(date=habit.start_date + timedelta(days=i)).exists()
        ]

        # Create the new Daily instances
        Daily.objects.bulk_create(new_daily_records)

        # Delete the Daily instances that are no longer needed
        daily_records.exclude(date__range=(habit.start_date, habit.end_date)).delete()
    else:
        # Update the existing Daily instances with the updated dates
        for i, daily_record in enumerate(daily_records):
            daily_record.date = habit.start_date + timedelta(days=i)
            daily_record.save()
