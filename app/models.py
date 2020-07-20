from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from app.signals import post_save_user, pre_save_edit_book_date
from datetime import datetime
# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=100)
    birth_day = models.DateField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'user'
        ordering = ['full_name']

    def __str__(self):
        return f'{self.full_name} {self.middle_name}'

    def get_absolute_url(self):
        return reverse('user_books', kwargs={'user_id': self.id})
        
post_save.connect(post_save_user, sender = User)  


class Book(models.Model):
    reader = models.ForeignKey('User', on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    author_full_name = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    cost = models.FloatField()
    pages = models.IntegerField()
    create_date = models.DateField(default=timezone.now)
    edit_date = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'book'
        ordering = ['book_name']

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('edit_book', kwargs={'book_id': self.id})

pre_save.connect(pre_save_edit_book_date, sender = Book)
