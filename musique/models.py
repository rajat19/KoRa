import os
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify

class SongArtist(models.Model):
	slug = models.SlugField(max_length=40, unique=True)
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=50, null=True, blank=True)
	popularity = models.IntegerField(default=0)
	photo = models.FileField(default='', null=True, blank=True)
	photo_url = models.CharField(null=True, blank=True, max_length=250)
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		if not self.createdAt:
			self.createdAt = timezone.now()

		self.updatedAt = timezone.now()
		super(SongArtist, self).save(*args, **kwargs)

class SongGenre(models.Model):
	slug = models.SlugField(max_length=40, unique=True)
	name = models.CharField(max_length=100)
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		if not self.createdAt:
			self.createdAt = timezone.now()

		self.updatedAt = timezone.now()
		super(SongGenre, self).save(*args, **kwargs)

class SongAlbum(models.Model):
	slug = models.SlugField(max_length=40, unique=True)
	artist = models.ForeignKey(SongArtist)
	name = models.CharField(max_length=250, unique=True)
	release_date = models.DateField(null=True, blank=True)
	genre = models.ManyToManyField(SongGenre)
	logo = models.FileField(null=True, blank=True)
	logo_url = models.CharField(null=True, blank=True, max_length=250)
	popularity = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		if not self.createdAt:
			self.createdAt = timezone.now()

		self.updatedAt = timezone.now()
		super(SongAlbum, self).save(*args, **kwargs)

class Song(models.Model):
	slug = models.SlugField(max_length=40, unique=True)
	name = models.CharField(max_length=250)
	artist = models.ForeignKey(SongArtist, on_delete=models.CASCADE)
	album = models.ForeignKey(SongAlbum, on_delete=models.CASCADE)
	genre = models.ManyToManyField(SongGenre)
	language = models.CharField(max_length=40, null=True)
	duration = models.CharField(max_length=10, null=True)
	likes = models.IntegerField(default=0)
	times_played = models.IntegerField(default=0)
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.artist = self.album.artist
		if not self.id:
			self.slug = slugify(self.name)
		if not self.createdAt:
			self.createdAt = timezone.now()
			
		self.updatedAt = timezone.now()
		super(Song, self).save(*args, **kwargs)

class SongUpload(models.Model):
	song = models.ForeignKey(Song, null=True)
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField()
	no_of_downloads = models.CharField(max_length=5, default='0')
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def extension(self):
		fname, extension = os.path.splitext(self.file.name)
		return extension

	def save(self, *args, **kwargs):
		if not self.createdAt:
			self.createdAt = timezone.now()

		self.updatedAt = timezone.now()
		return super(SongUpload, self).save(*args, **kwargs)

class SongReview(models.Model):
	song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	review = models.TextField(max_length=1000)
	createdAt = models.DateTimeField(null=True, blank=True)
	updatedAt = models.DateTimeField(auto_now = True, null=True, blank=True)
	deletedAt = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.review

	def save(self, *args, **kwargs):
		if not self.createdAt:
			self.createdAt = timezone.now()

		self.updatedAt = timezone.now()
		return super(SongReview, self).save(*args, **kwargs)
