from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse######

from app.models import User
from app.models import Book

from app.forms import NewUserForm
from app.forms import NewBookForm
from app.forms import EditBookForm

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class BaseListView(ListView):
    model = User
    template_name = 'base.html'
class BaseDetailView(DetailView):
	model = User
	def get_context_data(self,**kwargs):
	    context = super().get_context_data(**kwargs)
	    context['books'] = Book.objects.filter(reader = self.kwargs['pk'])
	    context['reader'] = User.objects.get(id = self.kwargs['pk'])
	    return context
	template_name = 'book.html'

class BaseFormView(CreateView):
	form_class = NewUserForm
	success_url = '/'
	template_name = 'base.html'
	def post(self , request , *args , **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)


"""
def base_view(request):
	users = User.objects.all()
	form = NewUserForm(request.POST or None)
	if form.is_valid():
		full_name = form.cleaned_data['full_name']
		birth_day = form.cleaned_data['birth_day']
		phone = form.cleaned_data['phone']
		new_user = User.objects.create(full_name = full_name, birth_day = birth_day, phone = phone)
		return HttpResponseRedirect(reverse('base'))

	context = {
	'users': users,
	'form': form
	}
	return render(request, 'base.html', context)
"""

def book_view(request, user_id):
	books = Book.objects.filter(reader=user_id)
	reader = User.objects.get(id = user_id)
	form = NewBookForm(request.POST or None)
	if form.is_valid():
		book_name = form.cleaned_data['book_name']
		author_full_name = form.cleaned_data['author_full_name']
		year = form.cleaned_data['year']
		new_book = Book.objects.create(reader= reader,book_name = book_name, author_full_name = author_full_name, year = year)
		return HttpResponseRedirect('/book/'+user_id+'/')

	context = {
	'books': books,
	'reader': reader,
	'form': form
	}
	return render(request, 'book.html', context)


def edit_view(request, book_id):
	book = Book.objects.get(id = book_id)
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