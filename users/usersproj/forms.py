from django import forms
from . import models
from django.contrib.auth.forms import AdminPasswordChangeForm, AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User

forms.fields.Field.default_error_messages = {'required': ''}

class LoginUserForm:
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )




class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Кочанов'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'username': forms.TextInput(attrs={'placeholder': 'User'}),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'username': '',
        }
        help_texts = {
            'username': None,
            'password1': None,
        }
        field_classes = {'username': UsernameField}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['user', 'create_date']
        fields = ['birthday']
        widgets = {
            'birthday': forms.TextInput(attrs={'placeholder':'День рождения: мм/дд/гг'}),
        }
        labels = {
            'birthday': '',
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = ['name_gallery']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = models.Avatar
        fields = ['image']


class ShelfForm(forms.ModelForm):
    class Meta:
        model = models.Shelf
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'book']

class BookFormValid(forms.ModelForm):
    class Meta:
        model = models.BookAdmin
        fields = ['want_read', 'read', 'i_read']


class RedBook(forms.Form):
    title = forms.CharField(max_length=500)
    author = forms.CharField(max_length=500)


class Page(forms.Form):
    page_num = forms.IntegerField()
