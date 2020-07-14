from django.test import TestCase

from app.models import User
from app.models import Book

import datetime


class TestModelUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(full_name='Иванов Иван', middle_name='Иванович', birth_day=datetime.date(
            1997, 5, 2), phone='+375(29)508-80-02')

    def test_full_name_label(self):
        user = User.objects.get(id=1)
        # Получение метаданных поля для получения необходимых значений
        field_label = user._meta.get_field('full_name').verbose_name
        # Сравнить значение с ожидаемым результатом
        self.assertEquals(field_label, 'full name')

    def test_birth_day_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('birth_day').verbose_name
        self.assertEquals(field_label, 'birth day')
        # метод assertEquals() вместо assertTrue(), потому что, в случае провала теста, в выводе будет указано
        # какое именно значение содержит метка и это немного облегчит нам задачу по отладке кода.

    def test_phone_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_full_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 200)

    def test_phone_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)

    def test_str_is_full_name(self):
        user = User.objects.get(id=1)
        expected_object_name = '%s' % (user.full_name + ' ' + user.middle_name)
        self.assertEquals(expected_object_name, str(user))

    def test_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.get_absolute_url(), '/book/1/')


class TestModelBook(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=2, full_name='Иванов Иван', middle_name='Иванович', birth_day=datetime.date(
            1997, 5, 2), phone='+375(29)508-80-02')
        Book.objects.create(reader=user, book_name='Чистый код',
                            author_full_name='Роберт Мартин', year=2020)

    def test_book_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('book_name').verbose_name
        self.assertEquals(field_label, 'book name')

    def test_author_full_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author_full_name').verbose_name
        self.assertEquals(field_label, 'author full name')

    def test_year_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('year').verbose_name
        self.assertEquals(field_label, 'year')

    def test_reader_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('reader').verbose_name
        self.assertEquals(field_label, 'reader')

    def test_book_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('book_name').max_length
        self.assertEquals(max_length, 200)

    def test_author_full_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author_full_name').max_length
        self.assertEquals(max_length, 200)

    def test_year_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('year').max_length
        self.assertEquals(max_length, 4)

    def test_str_is_book_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = '%s' % (book.book_name)
        self.assertEquals(expected_object_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/edit_book/1/')
