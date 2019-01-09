from datetime import date
from django.db import models


class Book(models.Model):
    """Represents a book in the system.
    """
    cover_image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    YEARS = [(y, y) for y in range(date.today().year, 1453, -1)]
    year = models.IntegerField(default=date.today().year, choices=YEARS)
    AVAILABILITIES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-Out')
    ]
    status = models.CharField(
        max_length=128, default='available', choices=AVAILABILITIES)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    last_borrowed = models.DateField()

    def __str__(self):
        return f'{self.title} ({ self.status })'
