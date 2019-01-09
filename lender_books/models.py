from django.db import models


class Book(models.Model):
    """Represents a book in the system.
    """
    cover_image = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    year = models.IntegerField()
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
