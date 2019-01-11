from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Book(models.Model):
    """Represents a book in the system.
    """
    cover_image = models.ImageField(
        upload_to=settings.IMAGE_DIR)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    YEARS = [(y, y) for y in range(date.today().year, 1453, -1)]
    year = models.IntegerField(default=date.today().year, choices=YEARS)
    AVAILABILITIES = [
        ('available', 'Available'),
        ('checked-out', 'Checked-Out')
    ]
    status = models.CharField(
        max_length=128, default='available', choices=AVAILABILITIES)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    last_borrowed = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} ({ self.status })'
