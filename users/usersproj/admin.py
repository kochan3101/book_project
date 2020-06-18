from django.contrib import admin
from . import models
from django.contrib.auth.models import User
# Register your models here.

#admin.site.register(User)
admin.site.register(models.Profile)
admin.site.register(models.BookAdmin)
admin.site.register(models.Book)