from .models import Artist, Album, Song, Upload, Review
from django import form, template

class SongForm(forms.ModelForm):
    fields = ['name', 'album']

    def __init__(self, *args, **kwargs):
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['album'].empty_label = 'None'

    class Meta:
        model = Book
        fields = ['name', 'album']

class UploadForm(forms.ModelForm):
    fields = ['song', 'file']

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['song'].empty_label = ''

    class Meta:
        model = Upload
        fields = ['song', 'file']

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['song', 'reviewer', 'review', 'createdAt', 'deletedAt']

# class SearchForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Search
# 		fields = ['query']
