from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()


class Gallery(models.Model):
    photo_in_gallery = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    name_gallery = models.CharField(max_length=50, default='Мои Фотографии')

class ShelfAdmin(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"






class Avatar(models.Model):
    profile_avatar = models.ForeignKey(Gallery, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    class Meta:

        permissions = [
            ("usersproj.add_avatar", "usersproj.ADD_AVATAR")
        ]


class Shelf(models.Model):
    profile = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    page_num = models.IntegerField(default=0)
    book = models.FileField(upload_to='books/', null=True, blank=True)


    def __str__(self):
        return f"{self.title}, {self.page_num}"



class BookAdmin(models.Model):
    shelf = models.ManyToManyField(Shelf, blank=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    page_num = models.IntegerField(default=0)
    book = models.FileField(upload_to='books/', null=True, blank=True)
    book_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    want_read = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    i_read = models.BooleanField(default=False)