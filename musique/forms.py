from .models import SongArtist, SongAlbum, Song, SongUpload, SongReview
from django import forms, template

class SongForm(forms.ModelForm):
    fields = ['name', 'album']

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['album'].empty_label = 'None'

    class Meta:
        model = Song
        fields = ['name', 'album']

class UploadForm(forms.ModelForm):
    fields = ['song', 'file']

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['song'].empty_label = ''

    class Meta:
        model = SongUpload
        fields = ['song', 'file']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = SongReview
        fields = ['song', 'reviewer', 'review', 'createdAt', 'deletedAt']

class AlbumForm(forms.ModelForm):
    fields = ['artist', 'name', 'release_date', 'genre', 'logo', 'popularity', 'rating']

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['artist'].empty_label = 'None'

    class Meta:
        model = SongAlbum
        fields = ['artist', 'name', 'release_date', 'genre', 'logo', 'popularity', 'rating']


# class SearchForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Search
# 		fields = ['query']
