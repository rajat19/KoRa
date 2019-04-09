from .models import Book, BookUpload, BookReview, BookSearch
from django import forms, template


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['series'].empty_label = 'None'
        self.fields['author'].empty_label = ''
        self.fields['language'].empty_label = ''

    class Meta:
        model = Book
        fields = Book.db_fields()


class UploadForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['book'].empty_label = ''

    class Meta:
        model = BookUpload
        fields = BookUpload.db_fields()


class ReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        fields = BookReview.db_fields()


class SearchForm(forms.ModelForm):

    class Meta:
        model = BookSearch
        fields = BookSearch.db_fields()
