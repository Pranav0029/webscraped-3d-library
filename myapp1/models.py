from django.db import models
from django.utils import timezone


from myapp.models import Book

class Student_Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    lib_card_no = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='student_photos/')
    login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.lib_card_no})"

from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} -> {self.book.title}"
