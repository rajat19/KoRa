from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import View
from .forms import SongForm, AlbumForm, ReviewForm, UploadForm
from .models import SongArtist, SongAlbum, Song, SongUpload, SongReview

decorators = [login_required]

class IndexView(generic.ListView):
    template_name = 'musique/index.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all().order_by('name')

class SongView(generic.DetailView):
    model = Song
    template_name = 'musique/detail.html'

@method_decorator(login_required, name="dispatch")
class SongCreate(CreateView):
	form_class = SongForm
	template_name = 'musique/song_form.html'

@method_decorator(login_required, name="dispatch")
class SongUpdate(UpdateView):
	model = Song
	template_name = 'musique/song_update_form.html'
	fields = ['name', 'album']

@method_decorator(login_required, name="dispatch")
class SongDelete(DeleteView):
	model = Song
	success_url = reverse_lazy('musique:index')

@method_decorator(login_required, name="dispatch")
class SongUpload(View):
	form_class = UploadForm
	template_name = 'musique/upload_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, request.FILES)

		if form.is_valid():
			upload = form.save(commit=False)
			upload.uploader = request.user
			upload.save()

		return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class ReviewCreate(View):
	form_class = ReviewForm
	template_name = 'musique/detail.html'

	def get(self, request):
		pass

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			review = form.save(commit=False)
			review.reviewer = request.user
			review.song = form.cleaned_data['song']
			print(review)
			review.save()

		else:
			print(request.user)
			print('error in form')
			return render(request, 'musique/test.html', {'errors': form.errors})

		return redirect('musique:detail', slug=form.cleaned_data['song'].slug)

class ArtistList(generic.ListView):
    template_name = 'musique/artists.html'
    context_object_name = 'all_artists'

    def get_queryset(self):
        return SongArtist.objects.all().order_by('popularity')

class ArtistView(generic.DetailView):
    model = SongArtist
    template_name = 'musique/artist.html'

@method_decorator(login_required, name="dispatch")
class ArtistCreate(CreateView):
    model = SongArtist
    fields = ['name', 'country']

@method_decorator(login_required, name="dispatch")
class ArtistUpdate(UpdateView):
	model = SongArtist
	template_name = 'musique/artist_update_form.html'
	fields = ['name', 'country', 'popularity']

@method_decorator(login_required, name="dispatch")
class ArtistDelete(DeleteView):
	model = SongArtist
	success_url = reverse_lazy('musique:artists')

class AlbumList(generic.ListView):
    template_name = 'musique/albums.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return SongAlbum.objects.all().order_by('popularity')

class AlbumView(generic.DetailView):
    model = SongAlbum
    template_name = 'musique/album.html'

@method_decorator(login_required, name="dispatch")
class AlbumCreate(CreateView):
    form_class = AlbumForm
    template_name = 'musique/album_form.html'

@method_decorator(login_required, name="dispatch")
class AlbumUpdate(UpdateView):
	model = SongAlbum
	template_name = 'musique/album_update_form.html'
	fields = ['artist', 'title', 'released_date', 'genre', 'logo', 'popularity', 'rating']

@method_decorator(login_required, name="dispatch")
class AlbumDelete(DeleteView):
	model = SongAlbum
	success_url = reverse_lazy('musique:albums')

class SearchEverything(generic.ListView):
	template_name = 'musique/result.html'
	context_object_name = 'all_data'
	def get_queryset(self):
		searchString = self.request.GET.get('search') or '-created'
		# queryString = super(SearchEverything, self).get_queryset()
		songs = Song.objects.filter(title__contains=searchString)
		albums = SongAlbum.objects.filter(name__contains=searchString)
		artists = SongArtist.objects.filter(title__contains=searchString)
		data = {
			'artists': artists,
			'albums': albums,
			'songs': songs,
			'search_text': searchString
		}
		return data
