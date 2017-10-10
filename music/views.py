from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.timezone import utc
from django.views.generic import View
from .models import Artist, Album, Song, Upload, Review

decorators = [login_required]

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all().order_by('name')

class DetailView(generic.DetailView):
    model = Song
    template_name = 'music/detail.html'

@method_decorator(login_required, name="dispatch")
class SongCreate(CreateView):
	form_class = SongForm
	template_name = 'music/song_form.html'

@method_decorator(login_required, name="dispatch")
class SongUpdate(UpdateView):
	model = Song
	template_name = 'music/song_update_form.html'
	fields = ['name', 'album']

@method_decorator(login_required, name="dispatch")
class SongDelete(DeleteView):
	model = Song
	success_url = reverse_lazy('music:index')

@method_decorator(login_required, name="dispatch")
class SongUpload(View):
	form_class = UploadForm
	template_name = 'music/upload_form.html'

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
	template_name = 'music/detail.html'

	def get(self, request):
		pass

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			review = form.save(commit=False)
			review.reviewer = request.user
			review.book = form.cleaned_data['book']
			print(review)
			review.save()

		else:
			print(request.user)
			print('error in form')
			return render(request, 'music/test.html', {'errors': form.errors})

		return redirect('music:detail', slug=form.cleaned_data['song'].slug)
