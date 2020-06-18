# Generated by Django 3.0.5 on 2020-05-28 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersproj', '0012_avatar_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo_in_gallery',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
