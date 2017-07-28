# from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /books/2
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

	# /books/add/
	url(r'^add/$', views.BookCreate.as_view(), name='book-add'),

	# /books/upload/
	url(r'^upload/$', views.BookUpload.as_view(), name='upload'),

	# /books/1/review/add
	url(r'^review/add/$', views.ReviewCreate.as_view(), name='review-add'),

	# /books/2/update
	url(r'^(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name='book-update'),

	# /books/2/delete
	url(r'^(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),

	# /books/series/list
	url(r'^series/list$', views.SeriesList.as_view(), name="series-list"),

	# /books/series/2
	url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesView.as_view(), name="series"),

	# /books/series/add
	url(r'^series/add$', views.SeriesCreate.as_view(), name="series-add"),

	# /books/series/2/delete
	# url(r'^series/(?P<pk>[0-9]+)/delete/$', views.SeriesDelete.as_view(), name="series-delete"),

	# search/
	url(r'^search/$', views.SearchEverything.as_view(), name="search"),

	# /books/authors
	url(r'^authors/$', views.AuthorsView.as_view(), name='authors'),

	# /books/author/Jeffrey Archer
	url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorView.as_view(), name="author"),

	# /books/author/add
	url(r'^author/add$', views.AuthorCreate.as_view(), name="author-add"),
]
