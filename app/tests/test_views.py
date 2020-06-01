from django.test import TestCase

from app.models import User
from app.models import Book

import datetime
from django.urls import reverse

class TestBaseView(TestCase):

	
	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_accessible_by_name(self):
		resp = self.client.get(reverse('base'))
		self.assertEqual(resp.status_code, 200)

	def test_view_url_accessible_by_name(self):
		resp = self.client.get(reverse('base'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'base.html')

class TestBookView(TestCase):

	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(id = 2, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')

	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/book/2/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/book/2/')
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'base.html')


class TestEditView(TestCase):

	@classmethod
	def setUpTestData(cls):
		user = User.objects.create(id = 2, full_name = 'Иванов Иван Иванович', birth_day = datetime.date(1997, 5, 2), phone = '+375(29)508-80-02')
		Book.objects.create(id = 2,reader = user, book_name = 'Чистый код', author_full_name = 'Роберт Мартин', year = 2020)

	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/edit_book/2/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_exists_at_desired_location(self):
		resp = self.client.get('/edit_book/2/')
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'edit_book.html')