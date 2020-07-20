from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import User, Book

from app.forms import NewUserForm, EditUserForm, NewBookForm, EditBookForm


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


def edit_user_view(request, user_id):
    user = User.objects.get(id=user_id)
    form = EditUserForm(user, request.POST or None)
    if form.is_valid():
        full_name = form.cleaned_data['full_name']
        birth_day = form.cleaned_data['birth_day']
        phone = form.cleaned_data['phone']
        middle_name = form.cleaned_data['middle_name']
        email = form.cleaned_data['email']
        user.full_name = full_name
        user.birth_day = birth_day
        user.phone = phone
        user.middle_name = middle_name
        user.email = email
        user.save()
        return HttpResponseRedirect('/edit_user/'+str(user.id)+'/')

    context = {
        'user': user,
        'form': form
    }
    return render(request, 'edit_user.html', context)


def remove_user_view(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    return HttpResponseRedirect(reverse('base'))


def book_view(request, user_id):
    books = Book.objects.filter(reader=user_id)
    reader = User.objects.get(id=user_id)
    form = NewBookForm(request.POST or None)
    if form.is_valid():
        book_name = form.cleaned_data['book_name']
        author_full_name = form.cleaned_data['author_full_name']
        year = form.cleaned_data['year']
        cost = form.cleaned_data['cost']
        pages = form.cleaned_data['pages']
        Book.objects.create(
            reader=reader, book_name=book_name, author_full_name=author_full_name, year=year, cost=cost, pages=pages)
        return HttpResponseRedirect('/book/'+user_id+'/')

    context = {
        'books': books,
        'reader': reader,
        'form': form
    }
    return render(request, 'book.html', context)


def edit_book_view(request, book_id):
    book = Book.objects.get(id=book_id)
    form = EditBookForm(book, request.POST or None)
    if form.is_valid():
        book_name = form.cleaned_data['book_name']
        author_full_name = form.cleaned_data['author_full_name']
        year = form.cleaned_data['year']
        cost = form.cleaned_data['cost']
        pages = form.cleaned_data['pages']
        book.book_name = book_name
        book.author_full_name = author_full_name
        book.year = year
        book.cost = cost
        book.pages = pages
        book.save()
        return HttpResponseRedirect('/book/'+str(book.reader.id)+'/')

    context = {
        'book': book,
        'form': form
    }
    return render(request, 'edit_book.html', context)


def remove_book_view(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return HttpResponseRedirect('/book/'+str(book.reader.id)+'/')
