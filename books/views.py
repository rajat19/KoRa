from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Book, Series, Search
# from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name = 'all_books'

	def get_queryset(self):
		return Book.objects.all()

class DetailView(generic.DetailView):
	model = Book
	template_name = 'books/detail.html'

class BookCreate(CreateView):
	model = Book
	fields = ['author', 'book_title', 'country', 'language', 'genre', 'series_id', 'file']

class BookUpdate(UpdateView):
	model = Book
	fields = ['author', 'book_title', 'country', 'language', 'genre', 'series_id', 'file']

class BookDelete(DeleteView):
	model = Book
	success_url = reverse_lazy('books:index')

class SeriesView(generic.DetailView):
	model = Series
	template_name = 'books/series.html'

class SeriesCreate(CreateView):
	model = Series
	fields = ['series_title', 'no_of_books']

class SearchBook(View):
	model = Search

	def post(self, request):
		pass