from django.conf.urls import url
from . import views

app_name = 'musique'

urlpatterns = [
    # /musique/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /musique/songs
    url(r'^songs/$', views.SongList.as_view(), name='songs'),

    # /musique/song/in-the-end
    url(r'^song/(?P<slug>[\w-]+)/$', views.SongView.as_view(), name='detail'),

    # /musique/song/add
    url(r'^song/add/$', views.SongCreate.as_view(), name='song-add'),

    # /musique/song/in-the-end/update
    url(r'^song/(?P<slug>[\w-]+)/$', views.SongUpdate.as_view(), name='song-update'),

    # /musique/upload
    url(r'^upload/$', views.SongUpload.as_view(), name='upload'),

    # /musique/review/add
    url(r'^review/add/$', views.ReviewCreate.as_view(), name='review-add'),

    # /musique/song/in-the-end/delete
    url(r'^song/(?P<slug>[\w-]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /musique/artists
    url(r'^artists/$', views.ArtistList.as_view(), name='artists'),

    # /musique/artist/linkin-park
    url(r'^artist/(?P<slug>[\w-]+)/$', views.ArtistView.as_view(), name='artist'),

    # /musique/artist/add
    url(r'^artist/add/$', views.ArtistCreate.as_view(), name='artist-add'),

    # /musique/artist/linkin-park/update
    url(r'^artist/(?P<slug>[\w-]+)/update/$', views.ArtistUpdate.as_view(), name='artist-update'),

    # /musique/artist/linkin-park/delete
    url(r'^artist/(?P<slug>[\w-]+)/delete/$', views.ArtistDelete.as_view(), name='artist-delete'),

    # /musique/albums
    url(r'^albums/$', views.AlbumList.as_view(), name='albums'),

    # /musique/album/meteora
    url(r'^album/(?P<slug>[\w-]+)/$', views.AlbumView.as_view(), name='album'),

    # /musique/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /musique/album/meteora/update
    url(r'^album/(?P<slug>[\w-]+)/update/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /musique/album/meteora/delete
    url(r'^album/(?P<slug>[\w-]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # search/
    url(r'^search/$', views.SearchEverything.as_view(), name="search"),
]
