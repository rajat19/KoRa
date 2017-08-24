from django.contrib import admin
from .models import Album, Artist, Song, Upload, Review

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Upload)
admin.site.register(Review)
