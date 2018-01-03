from .models import Book, BookUpload, BookReview, BookSearch
from django import forms, template

class BookForm(forms.ModelForm):
	fields = ['series', 'author', 'title', 'language', 'genre', 'logo_file']

	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		self.fields['series'].empty_label = 'None'
		self.fields['author'].empty_label = ''
		self.fields['language'].empty_label = ''

	class Meta:
		model = Book
		fields = ['series', 'author', 'title', 'language', 'genre', 'synopsis', 'logo_file']

class UploadForm(forms.ModelForm):
	fields = ['book', 'file']

	def __init__(self, *args, **kwargs):
		super(UploadForm, self).__init__(*args, **kwargs)
		self.fields['book'].empty_label = ''

	class Meta:
		model = BookUpload
		fields = ['book', 'file']

class ReviewForm(forms.ModelForm):

	class Meta:
		model = BookReview
		fields = ['book', 'reviewer', 'review']

class SearchForm(forms.ModelForm):

	class Meta:
		model = BookSearch
		fields = ['query']
