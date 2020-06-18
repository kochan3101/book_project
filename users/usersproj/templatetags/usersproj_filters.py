from django.template.library import Library
from .. import models
from django.core.files import File

register = Library()


@register.simple_tag(name='book_filter')
def book_filter(book):
    book_valid_filter = ''
   #for book in book_valid:  # была итерация по books
    print(book.book)
    print(book.title)
    book_valid_filter = book_valid_filter + f'<h1>{book.author}</h1>' + f'<h1>{book.title}</h1>'
    with open(f'./media/{book.book.name}', 'r') as f:
        file = File(f)

        for line in file:
            book_valid_filter = book_valid_filter + f'<p>{line}</p>'

    return book_valid_filter


