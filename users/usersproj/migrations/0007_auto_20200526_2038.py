# Generated by Django 3.0.5 on 2020-05-26 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersproj', '0006_auto_20200526_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='profile_avatar',
        ),
        migrations.AddField(
            model_name='avatar',
            name='profile_avatar',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]