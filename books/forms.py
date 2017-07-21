from .models import Book, Series, Author, Upload, Review, Search
from django import forms, template

class BookForm(forms.ModelForm):
	fields = ['series', 'author', 'title', 'genre', 'logo_file']

	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		self.fields['series'].empty_label = 'None'
		self.fields['author'].empty_label = ''

	class Meta:
		model = Book
		fields = ['series', 'author', 'title', 'genre', 'synopsis', 'logo_file']

class UploadForm(forms.ModelForm):
	fields = ['book', 'file']

	def __init__(self, *args, **kwargs):
		super(UploadForm, self).__init__(*args, **kwargs)
		self.fields['book'].empty_label = ''

	class Meta:
		model = Upload
		fields = ['book', 'file']

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ['book', 'reviewer', 'review', 'createdAt', 'deletedAt']

class SearchForm(forms.ModelForm):

	class Meta:
		model = Search
<<<<<<< HEAD
		fields = ['query']
=======
		fields = ['searchedBy', 'query', 'searchedAt']
>>>>>>> c9f163058a01e5b7edfb4370281405363a6b1c48
