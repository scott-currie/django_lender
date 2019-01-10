from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Book


@login_required
def book_detail_view(request, pk=None):
    """Handle requests on /book/<id> and display a specific book.

    :input: request: incoming request
    :return: render the book detail template
    """
    context = {
        'book': get_object_or_404(Book, id=pk)
    }
    return render(request, 'books/book_detail.html', context)


@login_required
def book_list_view(request):
    """Handle requests on /book and display all books.

    :input: request: incoming request
    :return: render the book detail template
    """
    context = {
        'books': get_list_or_404(Book)
    }
    return render(request, 'books/book_list.html', context)
