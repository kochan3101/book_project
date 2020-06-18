# Generated by Django 3.0.5 on 2020-05-26 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersproj', '0009_auto_20200526_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo_in_gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]