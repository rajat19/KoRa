from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from .models import Book, Series, Search, Upload, Author
from .forms import BookForm, UploadForm

decorators = [login_required]

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name = 'all_books'

	def get_queryset(self):
		return Book.objects.all().order_by('title')

class DetailView(generic.DetailView):
	model = Book
	template_name = 'books/detail.html'

@method_decorator(login_required, name="dispatch")
class BookCreate(CreateView):
	form_class = BookForm
	template_name = 'books/book_form.html'

@method_decorator(login_required, name="dispatch")
class BookUpdate(UpdateView):
	form_class = BookForm
	template_name = 'books/book_form.html'

@method_decorator(login_required, name="dispatch")
class BookDelete(DeleteView):
	model = Book
	success_url = reverse_lazy('books:index')

@method_decorator(login_required, name="dispatch")
class BookUpload(View):
	form_class = UploadForm
	template_name = 'books/upload_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, request.FILES)

		if form.is_valid():
			upload = form.save(commit=False)
			upload.uploader = request.user
			upload.save()

		return render(request, self.template_name, {'form': form})

class SeriesList(generic.ListView):
	template_name = 'books/series_list.html'
	context_object_name = 'all_series'

	def get_queryset(self):
		return Series.objects.all().order_by('title')

class SeriesView(generic.DetailView):
	model = Series
	template_name = 'books/series.html'

@method_decorator(login_required, name="dispatch")
class SeriesCreate(CreateView):
	model = Series
	fields = ['title', 'no_of_books']

class SearchBook(View):
	model = Search
	template_name = 'books/result.html'

	def get(self, request):
		print(request.POST)
		# searched = Book.objects.get(title__contains='')
		return render(request, self.template_name)

	def post(self, request):
		pass

class AuthorsView(generic.ListView):
	template_name = 'books/authors.html'
	context_object_name = 'all_authors'

	def get_queryset(self):
		return Author.objects.all().order_by('name')

class AuthorView(generic.DetailView):
	model = Author
	template_name = 'books/author.html'

@method_decorator(login_required, name="dispatch")
class AuthorCreate(CreateView):
	model = Author
	fields = ['name', 'country']
