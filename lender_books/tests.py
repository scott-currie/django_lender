from datetime import datetime
from django.test import TestCase
from .models import Book


class TestBookModel(TestCase):
    """
    """

    def setUp(self):
        """
        """
        american_gods = {
            'cover_image': 'http://books.google.com/books/content?id=cLhVjQGs83QC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api',
            'title': "American Gods",
            'author': 'Neil Gaiman',
            'year': 2002,
            'status': 'available',
            'date_added': datetime.date(2019, 1, 1),
            'last_borrowed': datetime.date(2019, 1, 5)
        }

        book_1 = Book.objects.create(cover_image=american_gods['cover_image'],
                                     title=american_gods['title'],
                                     author=american_gods['author'],
                                     year=american_gods['year'],
                                     status=american_gods['status'],
                                     date_added=american_gods['date_added'],
                                     last_borrowed=american_gods['last_borrowed'])
