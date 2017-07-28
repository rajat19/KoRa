from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import View
from .models import Book, Series, Search, Upload, Author, Review
from .forms import BookForm, UploadForm, ReviewForm

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
	model = Book
	template_name = 'books/book_update_form.html'
	fields = ['series', 'title', 'author', 'language', 'genre', 'synopsis', 'logo_file']

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

class SearchEverything(generic.ListView):
	template_name = 'books/result.html'
	context_object_name = 'all_data'
	def get_queryset(self):
		searchString = self.request.GET.get('search') or '-created'
		# queryString = super(SearchEverything, self).get_queryset()
		books = Book.objects.filter(title__contains=searchString)
		authors = Author.objects.filter(name__contains=searchString)
		series = Series.objects.filter(title__contains=searchString)
		data = {'books': books, 'authors': authors, 'series': series, 'search_text': searchString}
		return data

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

@method_decorator(login_required, name='dispatch')
class ReviewCreate(View):
	form_class = ReviewForm
	template_name = 'books/detail.html'

	def get(self, request):
		pass

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			review = form.save(commit=False)
			review.reviewer = request.user
			review.book = form.cleaned_data['book']
			print(review)
			review.save()

		else:
			print(request.user)
			print('error in form')
			return render(request, 'books/test.html', {'errors': form.errors})

		return redirect('books:detail', pk=form.cleaned_data['book'].id)
