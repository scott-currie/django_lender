from datetime import datetime
from django.test import TestCase, RequestFactory
from .models import Book
from django_lender.views import home_view
from .views import book_detail_view, book_list_view
from django.contrib.auth.models import User

class TestBookModel(TestCase):
    """Test class for running tests on Book objects.
    """

    def setUp(self):
        """Set up some Book objects to serve as data for the test cases.

        :input: None
        :return: None
        """
        american_gods = {
            'cover_image': '',
            'title': "American Gods",
            'author': 'Neil Gaiman',
            'year': 2002,
            'status': 'available',
            'date_added': datetime(2019, 1, 1),
            'last_borrowed': datetime(2019, 1, 5)
        }

        Book.objects.create(cover_image=american_gods['cover_image'],
                            title=american_gods['title'],
                            author=american_gods['author'],
                            year=american_gods['year'],
                            status=american_gods['status'],
                            date_added=american_gods['date_added'],
                            last_borrowed=american_gods['last_borrowed'])

    def test_book_title(self):
        """Test that a book retrieved from setUp has expected title."""
        book = Book.objects.get(title='American Gods')
        self.assertEqual(book.title, 'American Gods')


class TestBookViews(TestCase):
    """Class for testing the views that display books."""

    def setUp(self):
        """Run some setup for tests that follow."""
        self.request = RequestFactory()
        self.test_user = User.objects.create_user('tester', 'tester@test.com', 'test321')
        american_gods = {
            'cover_image': '',
            'title': "American Gods",
            'author': 'Neil Gaiman',
            'year': 2002,
            'status': 'available',
            'date_added': datetime(2019, 1, 1),
            'last_borrowed': datetime(2019, 1, 5)
        }

        Book.objects.create(cover_image=american_gods['cover_image'],
                            title=american_gods['title'],
                            author=american_gods['author'],
                            year=american_gods['year'],
                            status=american_gods['status'],
                            date_added=american_gods['date_added'],
                            last_borrowed=american_gods['last_borrowed'])

    def test_book_list_view_status_code(self):
        """Test book_list view returns 200."""
        request = self.request.get('')
        # self.client.login(username='tester', password='test321')
        # request = self.client.get('')
        request.user = self.test_user
        response = book_list_view(request)
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_content(self):
        """Test book_list view returns expected HTML."""
        request = self.request.get('')
        request.user = self.test_user
        response = book_list_view(request)
        self.assertIn(b'<h2>Books</h2>', response.content)
        self.assertIn(b'<p>Neil Gaiman</p>', response.content)

    def test_book_detail_view_status_code(self):
        """Test book_detail_view."""
        request = self.request.get('')
        request.user = self.test_user
        book = Book.objects.get(title='American Gods')
        response = book_detail_view(request, pk=book.id)
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view_content(self):
        """Test book_detail_view."""
        request = self.request.get('')
        book = Book.objects.get(title='American Gods')
        request.user = self.test_user
        response = book_detail_view(request, pk=book.id)
        self.assertIn(b'<h3>American Gods</h3>', response.content)


class TestHomeView(TestCase):
    """Class to test generic views.
    """

    def setUp(self):
        """Do some setup for following tests."""
        self.request = RequestFactory()
        self.test_user = User.objects.create_user('tester', 'tester@test.com', 'test321')

    def test_home_view_status_code(self):
        """Check status code on home_view."""
        request = self.request.get('')
        request.user = self.test_user
        response = home_view(request)
        self.assertEqual(response.status_code, 200)

    def test_home_view_content(self):
        """Check expected HTML in response from home_view."""
        request = self.request.get('')
        request.user = self.test_user
        response = home_view(request)
        self.assertIn(b'Welcome to Book Lender', response.content)
