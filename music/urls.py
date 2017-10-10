from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/song/in-the-end
    url(r'^song/(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/song/add
    url(r'^song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /music/song/in-the-end/update
    url(r'^song/(?P<slug>[\w-]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /music/upload
    url(r'^upload/$', views.SongUpload.as_view(), name='upload'),

    # /music/review/add
    url(r'^review/add/$', views.ReviewCreate.as_view(), name='review-add'),

    # /music/song/in-the-end/delete
    url(r'^song/(?P<slug>[\w-]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /music/artist/linkin-park
    url(r'^artist/(?P<slug>[\w-]+)/$', views.ArtistView.as_view(), name='artist'),

    # /music/artist/add
    url(r'^artist/add/$', views.ArtistCreate.as_view(), name='artist-add'),

    # /music/artist/linkin-park/update
    url(r'^artist/(?P<slug>[\w-]+)/update/$', views.ArtistUpdate.as_view(), name='artist-update'),

    # /music/artist/linkin-park/delete
    url(r'^artist/(?P<slug>[\w-]+)/delete/$', views.ArtistDelete.as_view(), name='artist-delete'),

    # /music/album/meteora
    url(r'^album/(?P<slug>[\w-]+)/$', views.AlbumView.as_view(), name='album'),

    # /music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/meteora/update
    url(r'^album/(?P<slug>[\w-]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/meteora/delete
    url(r'^album/(?P<slug>[\w-]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
