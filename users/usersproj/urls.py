from django.urls import path
from . import views
from .views import RegistrationView,  logout_view, LoginUserView1, book_list, ShelfUserView, BookView, listshelf, book_list_on_shelf, NewItemView, GalleryUserView, listgallery, newimage, image_in_gallery, book_valid_ad_odinochestva, book_list_valid, shelf_list_for_book, one_book_on_shelf
from django.contrib.auth import login, logout

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='user'),
    path('login/', LoginUserView1.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', book_list_valid, name='book_list_valid'),
    path('book_list/', book_list, name='book_list'),
    path('listshelf/', listshelf, name='listshelf'),
    path('book_list_on_shelf/', book_list_on_shelf, name='book_list_on_shelf'),
   # path('add_item/', NewItemView.as_view(), name='add_item'),
    path('add_item/',  book_valid_ad_odinochestva, name='add_item'),
    path('newgallery/', GalleryUserView.as_view(), name='newgallery'),
    path('listgallery/', listgallery, name='listgallery'),
    path('newimage/', newimage, name='newimage'),
    path('image_in_gallery/', image_in_gallery, name='image_in_gallery'),
    path('newshelf/', ShelfUserView.as_view(), name='shelf'),
    path('shelf_list_for_book/', shelf_list_for_book, name='shelf_list_for_book'),
    path('one_book_on_shelf/', one_book_on_shelf, name='one_book_on_shelf'),

]
#urlpatterns = [
   # path('register/', RegistrationView.as_view(), name='user'),
   # path('login/', login, name='login'),
  #  path('login/', LoginUserView1.as_view(), name='login'),
   # path('logout/', logout_view, name='logout'),
   # path('', ShelfUserView.as_view(), name='shelf'),
   # path('book_list/', book_list, name='book_list'),
  #  path('listshelf/', listshelf, name='listshelf'),
  #  path('book_list_on_shelf/', book_list_on_shelf, name='book_list_on_shelf'),
   # path('add_item/', NewItemView.as_view(), name='add_item'),
   # path('add_item/',  book_valid_ad_odinochestva, name='add_item'),
   # path('newgallery/', GalleryUserView.as_view(), name='newgallery'),
  #  path('listgallery/', listgallery, name='listgallery'),
  #  path('newimage/', newimage, name='newimage'),
   # path('image_in_gallery/', image_in_gallery, name='image_in_gallery'),
  #  path('book_list_valid/', book_list_valid, name='book_list_valid'),
  #  path('shelf_list_for_book/', shelf_list_for_book, name='shelf_list_for_book'),
   # path('one_book_on_shelf/', one_book_on_shelf, name='one_book_on_shelf'),

#]