# Generated by Django 3.0.5 on 2020-06-06 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersproj', '0013_auto_20200528_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('profile_avatar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usersproj.Gallery')),
            ],
            options={
                'permissions': [('usersproj.add_avatar', 'usersproj.ADD_AVATAR')],
            },
        ),
    ]
