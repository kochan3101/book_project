from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.core.files import File

from . import models
from .forms import UserForm, ProfileForm, LoginUserForm, BookForm, ShelfForm, AvatarForm, GalleryForm
from django.contrib import auth
from . import forms
from .models import Shelf
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

#content_type = ContentType.objects.get_for_model(GalleryForm)
#my_permission = Permission.objects.create(codename='your_permission',
                                 #         name='Can access something',
                                     #     content_type=content_type)
#my_group = Group.objects.create(name='My Group')
#my_group.permissions = [my_permission]
#user.groups.add(my_group)
#user.has_perm('app_label.your_permission')  # True

class RegistrationView(TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        user_form = UserForm()
        profile_form = ProfileForm()
        avatar_form = AvatarForm()
        return ({'user_form': user_form,
                'profile_form': profile_form,
                 'avatar_form': avatar_form
                       })

    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        avatar_form = AvatarForm(request.POST, request.FILES)
        try:
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            gallery = models.Gallery.objects.create(photo_in_gallery=user)
            avatar = avatar_form.save(commit=False)
            print(gallery.name_gallery)
            print(avatar.image.url)
            avatar.profile_avatar = gallery
            avatar.save()
            user1 = auth.authenticate(username=user.username, password=user.password)
            user2 = User.objects.get(username=f'{user.username}')
            print(user.username)
            if user2 is not None:
               # send_mail('Subject here', f'Ваш логин: {user2.username},ваш пароль: '
                  #                        f'{user2.password}', 'kochan.arseniy17@gmail.com',
                    #      [f'{user2.email}'], fail_silently=False)
                auth.login(request, user2)
            else:
                return HttpResponse('Disabled account')
        except ValueError:
            return render(request, self.template_name, {'user_form': user_form,
                                                        'profile_form': profile_form,
                                                        'avatar_form': avatar_form
                                                                                     })
        return redirect('/')


class LoginUserView1(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        user_form = UserForm()
        return ({'user_form': user_form,
                       })

    def post(self, request):
       # user_form = LoginUserForm(request.POST)
        #username = user_form['username']
       # password = user_form['password2']
        try:
           # user_for = user_form
            #username = user_for.username
            #password = user_for.password
            #print(username)
            user1 = User.objects.get(username=f'{request.POST["username"]}')
            #print(username)
            #user1 = auth.authenticate(username=username, password=password)
            if user1 is not None:
                auth.login(request, user1)
            else:
                return HttpResponse('Disabled account')
        except ValueError:
            return render(request, self.template_name, {'user_form': user_form,
                                                                                     })
        return redirect('/')



def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли')


class GalleryUserView(TemplateView):
    template_name = 'gallery.html'

    def get(self, request, **kwargs):
        context = self.get_context_data(gallery_form=GalleryForm(), pk=request.GET.get('pk'))
        return self.render_to_response(context)

    def post(self, request):
        permission = Permission.objects.get(
            codename="add_avatar")
        print(permission.codename)
        request.user.user_permissions.add(permission)
        # перезагрузить
        request.user.refresh_from_db()
       # pk = request.GET.get('pk')
        gallery_form = GalleryForm(request.POST)
        print(request.user.username)
        try:
            user = models.User.objects.get(username=request.user.username)
            gallery = gallery_form.save(commit=False)
            gallery.photo_in_gallery = user
            gallery.save()
            return redirect('/')
            #return HttpResponse('Authenticated successfully')
        except ValueError:
            return render(request, self.template_name, {'gallery_form': gallery_form,
                                                            })
        #return redirect('/')

def listgallery(request):
    gallery = models.Gallery.objects.filter(photo_in_gallery=request.user)
    return render(request, 'listgallery.html', {'gallery': gallery})

def newimage(request):
  #  permission = Permission.objects.get(
   #     codename="add_avatar")
  #  print(permission.codename)
   # request.user.user_permissions.add(permission)
    # перезагрузить
   # request.user.refresh_from_db()
    print(request.user.get_user_permissions())
    if request.user.has_perm("usersproj.add_avatar"):
        if request.method == 'POST':
            gallery = models.Gallery.objects.get(photo_in_gallery=request.user, pk=request.GET.get('pk'))

            print(gallery.name_gallery)
            avatar_form = AvatarForm(request.POST, request.FILES)
            if avatar_form.is_valid():
                avatar = avatar_form.save(commit=False)
                if gallery is not None:
                    avatar.profile_avatar = gallery

                    avatar.save()
                    print(avatar.image)
                    return redirect('/')
                else:
                    return HttpResponse('noooo')

        else:
            avatar_form = AvatarForm()
            pk = request.GET.get('pk')

        return render(request, 'newimage.html', {'avatar_form': avatar_form, 'pk': pk})
    else:
        raise PermissionDenied()


#@login_required
class ShelfUserView(TemplateView):
    template_name = 'shelf.html'

    def get_context_data(self, **kwargs):
        shelf_form = ShelfForm()
        return ({'shelf_form': shelf_form,
                       })

    def post(self, request):
        shelf_form = ShelfForm(request.POST)
     #   print(request.POST['name'])
      #  print(request.user.username)
        try:
            user = User.objects.get(username=f'{request.user.username}')
       #     print(user.username)
            shelf = shelf_form.save(commit=False)
          #  print(user.username)
            shelf.profile = user
            shelf.save()
            return redirect(reverse('book_list') + f'?pk={shelf.pk}')
            #return HttpResponse('Authenticated successfully')
        except ValueError:
            return render(request, self.template_name, {'shelf_form': shelf_form,
                                                                                     })
        #return redirect('/')


class BookView(TemplateView):

    template_name = 'book_list.html'
    def get(self, request, **kwargs):
        book_form = BookForm()
        pk = request.GET.get('pk')
        context = self.get_context_data(book_form=BookForm(), pk=request.GET.get('pk'))
        return self.render_to_response(context)

    def post(self, request):
       # pk = request.GET.get('pk')
        book_form = BookForm(request.POST, request.FILES)
        print(request.user.username)
        try:
            shelf = models.Shelf.objects.get(profile=request.user, pk=request.GET.get('pk'))
            book = book_form.save(commit=False)
            book.shelf = shelf
            book.save()
            return redirect('/')
            #return HttpResponse('Authenticated successfully')
        except ValueError:
            return render(request, self.template_name, {'book_form': book_form,
                                                            })
        #return redirect('/')

def book_list(request):
    if request.method == 'POST':
        shelf = models.Shelf.objects.get(profile=request.user, pk=request.GET.get('pk'))

        print(shelf.profile.username)
        print(shelf.name)
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            if shelf is not None:
                book.shelf = shelf
                book.save()
                print(book.book.name)
                return redirect('/')
            else:
                return HttpResponse('noooo')

    else:
        book_form = BookForm()
        pk = request.GET.get('pk')

    return render(request, 'book_list.html', {'book_form': book_form, 'pk': pk})

def image_in_gallery(request):
    pk = request.GET.get('pk')
    gallery = models.Gallery.objects.get(photo_in_gallery=request.user, pk=pk)
    avatars = gallery.avatar_set.all()
    return render(request, 'image_in_gallery.html', {'avatars': avatars, 'pk': pk})

def listshelf(request):
    shelf = models.Shelf.objects.filter(profile=request.user)
    return render(request, 'listshelf.html', {'shelf': shelf})

def book_list_on_shelf(request):
    pk = request.GET.get('pk')
    shelf = models.Shelf.objects.get(profile=request.user, pk=pk)
    book_valid = """"""
    books = shelf.book_set.all()
    books_valid = shelf.bookadmin_set.all()
    for book in books_valid: # была итерация по books
        print(book.book.name)
        with open(f'./media/{book.book.name}', 'r') as f:
            file = File(f)
            for line in file:
                book_valid = book_valid + line
    #for book in books:
      #  print(book.book.name)
    return render(request, 'book_list_on_shelf.html', {'books': books, 'pk': pk,
                                                       'book_valid': book_valid,
                                                       'books_valid': books_valid,
                                                       'shelf': shelf
                                                       })



class NewItemView(TemplateView):

    template_name = 'add_item.html'
    def get(self, request, **kwargs):
        context = self.get_context_data(book_form=BookForm(), pk=request.GET.get('pk'))
        return self.render_to_response(context)

    def post(self, request):
       # pk = request.GET.get('pk')
        book_form = BookForm(request.POST, request.FILES)
        print(request.user.username)
        try:
            shelf = models.Shelf.objects.get(profile=request.user, pk=request.GET.get('pk'))
            book = book_form.save(commit=False)
            book.shelf = shelf
            book.save()
            request.user.refresh_from_db()
            print(book.book.name)
            return redirect('/')
            #return HttpResponse('Authenticated successfully')
        except ValueError:
            return render(request, self.template_name, {'book_form': book_form,
                                                            })
        #return redirect('/')

def book_valid_ad_odinochestva(request):
    shelf = models.Shelf.objects.get(profile=request.user, pk=request.GET.get('pk'))
    book = models.BookAdmin.objects.get(pk=request.GET.get('book_pk'))
    shelf.bookadmin_set.add(book)
    book.save()
    print(book.book.name)
    return redirect('/')

#def book_valid_v_strane_vodianih(request):
   # shelf = models.Shelf.objects.get(profile=request.user, name='Арсений')
    #book = models.BookAdmin.objects.get(title='В стране водяных')
    #shelf.bookadmin_set.add(book)
   # book.save()
   # print(book.book.name)
    #return redirect('/')

def book_list_valid(request):
    books = models.BookAdmin.objects.all()
    return render(request, 'book_list_valid.html', {'books': books,
                                                       })

def shelf_list_for_book(request):
    book_pk = request.GET.get('pk')
    print(book_pk)
    shelfs = models.Shelf.objects.filter(profile=request.user)
    return render(request, 'shelf_list_for_book.html', {'shelfs': shelfs,
                                                        'book_pk': book_pk
                                                       })


def one_book_on_shelf(request):
    shelf_pk = request.GET.get('shelf_pk')
    book_pk = request.GET.get('book_pk')
    shelf = models.Shelf.objects.get(profile=request.user, pk=shelf_pk)
    book = models.BookAdmin.objects.get(shelf=shelf, pk=book_pk)
    return render(request, 'one_book_on_shelf.html', {'book': book,

                                                       })


