# Generated by Django 3.2.20 on 2023-07-07 19:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, default='avatar.jpg', upload_to='profile_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=360)),
                ('category', models.CharField(choices=[('HEALTH', 'HEALTH'), ('FITNESS', 'FITNESS'), ('LEARNING', 'LEARNING'), ('DESTRUCTIVE', 'DESTRUCTIVE'), ('PRODUCTIVITY', 'PRODUCTIVITY'), ('SELF-CARE', 'SELF-CARE'), ('FINANCE', 'FINANCE'), ('RELATIONSHIP', 'RELATIONSHIP'), ('MINDFULNESS', 'MINDFULNESS')], default=None, max_length=20)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=None)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('done', models.BooleanField(default=False)),
                ('habit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='habitrain.habit')),
            ],
            options={
                'unique_together': {('habit', 'date')},
            },
        ),
    ]
