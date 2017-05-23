from django.db import models
from django.contrib.auth.models import User

class Series(models.Model):
	series_title = models.CharField(max_length=250)
	no_of_books = models.CharField(max_length=2)

class Book(models.Model):
	author = models.CharField(max_length=200)
	book_title = models.CharField(max_length=250)
	country = models.CharField(max_length=100, blank=True)
	language = models.CharField(max_length=100)
	genre = models.CharField(max_length=200)
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	series_id = models.ForeignKey(Series, null=True, blank=True)
	synopsis = models.TextField(max_length=500)
	year = models.DateField(null=True, blank=True)
	file = models.FileField(blank=True)
	file_type = models.CharField(max_length=4)
	book_logo = models.CharField(max_length=200)

class Search(models.Model):
	searched_by = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	date = models.DateTimeField(null=True)