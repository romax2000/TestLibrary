from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
 	id = models.AutoField(primary_key=True)
 	full_name = models.CharField(max_length=200, null = False)
 	birth_day = models.DateField(blank = False, null = False)
 	phone = models.CharField(max_length=20, blank=True, null=True)

 	class Meta:
 		db_table = 'user'
 		ordering = ['full_name']

 	def __str__(self):
 		return self.full_name

 	def get_absolute_url(self):
 		return reverse('user_books', kwargs={'user_id': self.id})

class Book(models.Model):
	id = models.AutoField(primary_key=True)
	reader = models.ForeignKey('User', on_delete=models.CASCADE)
	book_name = models.CharField(max_length=200, null = False)
	author_full_name = models.CharField(max_length=200, null = False)
	year = models.CharField(max_length=4, blank = False, null = False)

	class Meta:
		db_table = 'book'
		ordering = ['book_name']

	def __str__(self):
		return self.book_name

	def get_absolute_url(self):
 		return reverse('edit_book', kwargs={'book_id': self.id})