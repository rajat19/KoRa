from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=250, unique=True)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=100)
    logo = models.FileField()

    def __str__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length=250)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, null=True, blank=True)

class Upload(models.Model):
    song = models.ForeignKey(Song, null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    no_of_downloads = models.CharField(max_length=5, default='0')

	def extension(self):
		fname, extension = os.path.splitext(self.file.name)
		return extension

class Review(models.Model):
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
		return super(Review, self).save(*args, **kwargs)
