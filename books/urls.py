from django.conf.urls import url
from . import views


app_name = 'books'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /books/2
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

	# /books/add/
	url(r'^add/$', views.BookCreate.as_view(), name='book-add'),

	# /books/2/
	url(r'^(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),

	# /books/2/delete
	url(r'^(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),

	# /books/series/2
	url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesView.as_view(), name="series"),

	# /books/series/add
	url(r'^series/add/(?P<pk>[0-9]+)/$', views.SeriesCreate.as_view(), name="series-add"),

	# /books/series/2/delete
	# url(r'^series/(?P<pk>[0-9]+)/delete/$', views.SeriesDelete.as_view(), name="series-delete"),

	# search/harry potter
	# url(r'^search/(?P[a-zA-Z0-9 ]+)/$', views.SearchBook.as_view(), name="search"),
]