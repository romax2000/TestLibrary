from django.test import TestCase

import datetime

from app.models import User
from app.models import Book

from app.forms import NewUserForm
from app.forms import NewBookForm
from app.forms import EditBookForm

class TestNewUserForm(TestCase):

	def test_new_form_name_field_label(self):
		form = NewUserForm()
		self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'ФИО')

	def test_new_form_birth_day_field_label(self):
		form = NewUserForm()
		self.assertTrue(form.fields['birth_day'].label == None or form.fields['birth_day'].label == 'Дата рождения')

	def test_new_form_phone_field_label(self):
		form = NewUserForm()
		self.assertTrue(form.fields['phone'].label == None or form.fields['phone'].label == 'Номер телефона')

	def test_new_form_phone_field_initial(self):
		form = NewUserForm()
		self.assertTrue(form.fields['phone'].initial == '+375()--')

	def test_new_form_phone_field_help_text(self):
		form = NewUserForm()
		self.assertTrue(form.fields['phone'].help_text == 'Формат: +375(ХХ)ХХХ-ХХ-ХХ')

class TestNewBookForm(TestCase):

	def test_new_form_name_field_label(self):
		form = NewBookForm()
		self.assertTrue(form.fields['book_name'].label == None or form.fields['book_name'].label == 'Название книги')

	def test_new_form_author_field_label(self):
		form = NewBookForm()
		self.assertTrue(form.fields['author_full_name'].label == None or form.fields['author_full_name'].label == 'Автор')

	def test_new_form_year_field_label(self):
		form = NewBookForm()
		self.assertTrue(form.fields['year'].label == None or form.fields['year'].label == 'Год издания')

class TestEditBookForm(TestCase):

	def test_renew_form_name_field_label(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['book_name'].label == None or form.fields['book_name'].label == 'Название книги')

	def test_renew_form_author_field_label(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['author_full_name'].label == None or form.fields['author_full_name'].label == 'Автор')

	def test_renew_form_year_field_label(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['year'].label == None or form.fields['year'].label == 'Год издания')

	def test_renew_form_name_field_initial(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['book_name'].initial == 'Чистый код')

	def test_renew_form_author_field_initial(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['author_full_name'].initial == 'Роберт Мартин')

	def test_renew_form_year_field_initial(self):
		user = User.objects.create(id = 4, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		book = Book.objects.create(id = 4,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)
		form = EditBookForm(book)
		self.assertTrue(form.fields['year'].initial == 2020)