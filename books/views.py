from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Book, Series, Search, Upload
from .forms import BookForm, UploadForm

class IndexView(generic.ListView):
	template_name = 'books/index.html'
	context_object_name = 'all_books'

	def get_queryset(self):
		return Book.objects.all().order_by('title')

class DetailView(generic.DetailView):
	model = Book
	template_name = 'books/detail.html'

class BookCreate(CreateView):
	form_class = BookForm
	template_name = 'books/book_form.html'

class BookUpdate(UpdateView):
	model = Book
	fields = ['series', 'title', 'author', 'language', 'genre', 'synopsis', 'logo_file']

class BookDelete(DeleteView):
	model = Book
	success_url = reverse_lazy('books:index')

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

class SeriesView(generic.DetailView):
	model = Series
	template_name = 'books/series.html'

class SeriesCreate(CreateView):
	model = Series
	fields = ['title', 'no_of_books']

class SearchBook(View):
	model = Search

	def post(self, request):
		pass