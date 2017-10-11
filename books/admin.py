from django.contrib import admin
from .models import BookSeries, BookAuthor, Book, BookSearch, BookUpload, BookReview

admin.site.register(BookAuthor)
admin.site.register(BookSeries)
admin.site.register(Book)
admin.site.register(BookSearch)
admin.site.register(BookUpload)
admin.site.register(BookReview)
