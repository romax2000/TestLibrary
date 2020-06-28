from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import User
from app.models import Book

from app.forms import NewUserForm
from app.forms import NewBookForm
from app.forms import EditBookForm

# Create your views here.


def base_view(request):
    users = User.objects.all()
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        full_name = form.cleaned_data['full_name']
        birth_day = form.cleaned_data['birth_day']
        phone = form.cleaned_data['phone']
        middle_name = form.cleaned_data['middle_name']
        email = form.cleaned_data['email']
        User.objects.create(
            full_name=full_name, birth_day=birth_day, phone=phone, middle_name=middle_name, email=email)
        return HttpResponseRedirect(reverse('base'))

    context = {
        'users': users,
        'form': form
    }
    return render(request, 'base.html', context)


def book_view(request, user_id):
    books = Book.objects.filter(reader=user_id)
    reader = User.objects.get(id=user_id)
    form = NewBookForm(request.POST or None)
    if form.is_valid():
        book_name = form.cleaned_data['book_name']
        author_full_name = form.cleaned_data['author_full_name']
        year = form.cleaned_data['year']
        Book.objects.create(
            reader=reader, book_name=book_name, author_full_name=author_full_name, year=year)
        return HttpResponseRedirect('/book/'+user_id+'/')

    context = {
        'books': books,
        'reader': reader,
        'form': form
    }
    return render(request, 'book.html', context)


def edit_view(request, book_id):
    book = Book.objects.get(id=book_id)
    form = EditBookForm(book, request.POST or None)
    if form.is_valid():
        book_name = form.cleaned_data['book_name']
        author_full_name = form.cleaned_data['author_full_name']
        year = form.cleaned_data['year']
        book.book_name = book_name
        book.author_full_name = author_full_name
        book.year = year
        book.save()
        return HttpResponseRedirect('/book/'+str(book.reader.id)+'/')

    context = {
        'book': book,
        'form': form
    }
    return render(request, 'edit_book.html', context)
