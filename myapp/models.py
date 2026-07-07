from django.db import models
from django.utils import timezone

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Biography', 'Biography'),
        ('Children', 'Children'),
        ('Coding', 'Coding'),  # <-- Added this new category
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    published_year = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    cover_image = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title

    def is_custom_category(self):
        return self.category not in [choice[0] for choice in self.CATEGORY_CHOICES]
