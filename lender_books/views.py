from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Book


def book_detail_view(request, pk=None):
    """Handle requests on /book/<id> and display a specific book.

    :input: request: incoming request
    :return: render the book detail template
    """
    context = {
        'book': get_object_or_404(Book, id=pk)
    }
    return render(request, 'books/book_detail.html', context)


def book_list_view(request):
    """Handle requests on /book and display all books.

    :input: request: incoming request
    :return: render the book detail template
    """
    context = {
        'books': get_list_or_404(Book)
    }
    return render(request, 'books/book_list.html', context)
