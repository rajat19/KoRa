from django.contrib import admin
from .models import SongAlbum, SongArtist, Song, SongUpload, SongReview

admin.site.register(SongArtist)
admin.site.register(SongAlbum)
admin.site.register(Song)
admin.site.register(SongUpload)
admin.site.register(SongReview)
