import os
from django.db import models
from django.conf.global_settings import LANGUAGES
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import  slugify
from django_countries.fields import CountryField
from gdstorage.storage import GoogleDriveStorage
from common.models import SoftDeletionModel, TimestampModel

gd_storage = GoogleDriveStorage()


class BookSeries(SoftDeletionModel):
    slug = models.SlugField(max_length=40, unique=True)
    title = models.CharField(max_length=250, unique=True)
    no_of_books = models.CharField(max_length=2)

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('books:series')

    @staticmethod
    def db_fields():
        return ['title', 'no_of_books']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BookSeries, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'series'


class BookAuthor(SoftDeletionModel):
    slug = models.SlugField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    country = CountryField(blank_label='India')

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('books:author')

    @staticmethod
    def db_fields():
        return ['name', 'country']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(BookAuthor, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['name', 'country']


class Book(SoftDeletionModel):
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(BookAuthor, blank=True, default='')
    title = models.CharField(max_length=250)
    language = models.CharField(max_length=7, blank=True, null=True, choices=LANGUAGES)
    genre = models.CharField(max_length=200)
    series = models.ForeignKey(BookSeries, null=True, blank=True, default='')
    synopsis = models.TextField(max_length=1000)
    year = models.CharField(null=True, blank=True, max_length=4)
    logo = models.CharField(max_length=300, blank=True)
    logo_file = models.FileField(blank=True, upload_to='/book/logo', storage=gd_storage)

    def __str__(self):
        return self.title

    def logo_url(self):
        if self.logo:
            return self.logo
        if self.logo_file:
            url = self.logo_file.url
            new_url = url[:25] + 'uc?id=' + url[32:65]
            return new_url
        return False

    @staticmethod
    def get_absolute_url():
        return reverse('books:detail')

    @staticmethod
    def db_fields():
        return ['series', 'title', 'author', 'language', 'genre', 'synopsis', 'logo_file']

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Book._meta.fields]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['title', 'author']


class BookUpload(SoftDeletionModel):
    book = models.ForeignKey(Book, null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='/book/upload', storage=gd_storage)
    # file_type = models.CharField(max_length=4)
    no_of_downloads = models.CharField(max_length=5, default='0')

    def extension(self):
        file_name, extension = os.path.splitext(self.file.name)
        return extension

    @staticmethod
    def db_fields():
        return ['book', 'file']

    def save(self, *args, **kwargs):
        return super(BookUpload, self).save(*args, **kwargs)


class BookSearch(TimestampModel):
    searched_by = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=50, default='')
    searched_at = models.DateTimeField(null=True)

    @staticmethod
    def db_fields():
        return ['query']

    def save(self, *args, **kwargs):
        return super(BookSearch, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'search'


class BookReview(SoftDeletionModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.review

    @staticmethod
    def db_fields():
        return ['book', 'reviewer', 'review']

    def save(self, *args, **kwargs):
        return super(BookReview, self).save(*args, **kwargs)
