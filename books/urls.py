# from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /books/immortals
    url(r'^(?P<slug>[\w-]+)/$', views.BookView.as_view(), name="detail"),

    # /books/add/
    url(r'^add/$', views.BookCreate.as_view(), name='book-add'),

    # /books/upload/
    url(r'^upload/$', views.BookUpload.as_view(), name='upload'),

    # /books/review/add
    url(r'^review/add/$', views.ReviewCreate.as_view(), name='review-add'),

    # /books/immortals/update
    url(r'^(?P<slug>[\w-]+)/update/$', views.BookUpdate.as_view(), name='book-update'),

    # /books/immortals/delete
    url(r'^(?P<slug>[\w-]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),

    # /books/series/list
    url(r'^series/list$', views.SeriesList.as_view(), name="series-list"),

    # /books/series/shiva-trilogy
    url(r'^series/(?P<slug>[\w-]+)/$', views.SeriesView.as_view(), name="series"),

    # /books/series/add
    url(r'^series/add$', views.SeriesCreate.as_view(), name="series-add"),

    # /books/series/shiva-trilogy/delete
    # url(r'^series/(?P<slug>[\w-]+)/delete/$', views.SeriesDelete.as_view(), name="series-delete"),

    # search/
    url(r'^search/$', views.SearchEverything.as_view(), name="search"),

    # /books/authors
    url(r'^authors/$', views.AuthorsView.as_view(), name='authors'),

    # /books/author/jeffrey-archer
    url(r'^author/(?P<slug>[\w-]+)/$', views.AuthorView.as_view(), name="author"),

    # /books/author/add
    url(r'^author/add$', views.AuthorCreate.as_view(), name="author-add"),
]
