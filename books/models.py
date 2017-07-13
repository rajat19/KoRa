import os
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Series(models.Model):
	title = models.CharField(max_length=250, unique=True)
	no_of_books = models.CharField(max_length=2)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('books:series', kwargs={'pk': self.pk})

	class Meta:
		verbose_name_plural = 'series'

class Author(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('books:author', kwargs={'pk': self.pk})

	class Meta:
		unique_together = ['name', 'country']

class Book(models.Model):
	author = models.ForeignKey(Author, blank=True, default='')
	title = models.CharField(max_length=250)
	language = models.CharField(max_length=100, blank=True, null=True)
	genre = models.CharField(max_length=200)
	series = models.ForeignKey(Series, null=True, blank=True, default='')
	synopsis = models.TextField(max_length=1000)
	year = models.CharField(null=True, blank=True, max_length=4)
	logo = models.CharField(max_length=300, blank=True)
	logo_file = models.FileField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('books:detail', kwargs={'pk': self.pk})

	class Meta:
		unique_together = ['title', 'author']

class Upload(models.Model):
	book = models.ForeignKey(Book, null=True)
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField()
	# file_type = models.CharField(max_length=4)
	no_of_downloads = models.CharField(max_length=5, default='0')

	def extension(self):
		fname, extension = os.path.splitext(self.file.name)
		return extension

class Search(models.Model):
	searched_by = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	searchedAt = models.DateTimeField(null=True)

	class Meta:
		verbose_name_plural = 'search'

class Review(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.TextField(max_length=1000)
	createdAt = models.DateTimeField(null=True)
	deletedAt = models.DateTimeField(null=True)
