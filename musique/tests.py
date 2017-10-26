from django.test import TestCase
from .models import SongArtist, SongAlbum, Song

class SongArtistCase(TestCase):
    def setUp(self):
        SongArtist.objects.create(name = 'One Republic', country = 'USA')

    def test_slug_generated(self):
        """Check if slug generated successfully"""
        artist = SongArtist.objects.get(name = 'One Republic')
        self.assertEqual(artist.slug, 'one-republic')

class SongAlbumCase(TestCase):
    def setUp(self):    
        SongArtist.objects.create(name = 'One Republic', country = 'USA')
        artist = SongArtist.objects.get(name = 'One Republic')
        artist.songalbum_set.create(
            name = 'Native',
            release_date = '2013-03-22'
        )
        
    def test_slug_generated(self):
        """Check if slug generated successfully"""
        artist = SongAlbum.objects.get(name = 'Native')
        self.assertEqual(artist.slug, 'native')

# class SongCase(TestCase):
#     def setUp(self):
#         Song.objects.create(name = 'One Republic', country = 'USA')

#     def test_slug_generated(self):
#         """Check if slug generated successfully"""
#         artist = Song.objects.get(name = 'One Republic')
#         self.assertEqual(artist.slug, 'charlie-puth')