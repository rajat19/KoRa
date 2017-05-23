from django.contrib import admin
from .models import Series, Book, Search

admin.site.register(Book)
admin.site.register(Series)
admin.site.register(Search)