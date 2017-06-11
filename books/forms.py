from .models import Book, Series, Author, Upload
from django import forms, template

class BookForm(forms.ModelForm):
	fields = ['series', 'author', 'title', 'genre', 'logo_file']

	def __init__(self, *args, **kwargs):
		super(BookForm, self).__init__(*args, **kwargs)
		self.fields['series'].empty_label = 'None'
		self.fields['author'].empty_label = ''

	class Meta:
		model = Book
		fields = ['series', 'author', 'title', 'genre', 'logo_file']

class UploadForm(forms.ModelForm):
	fields = ['book', 'file']

	def __init__(self, *args, **kwargs):
		super(UploadForm, self).__init__(*args, **kwargs)
		self.fields['book'].empty_label = ''

	class Meta:
		model = Upload
		fields = ['book', 'file']