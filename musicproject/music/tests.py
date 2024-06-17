from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Album, Artist

class ArtistTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='mandy_admin', password='password', email='admin@example.com')
        self.artist = Artist.objects.create(name='Empire Of The Sun', genre='Indie', popularity=1)

    def test_create_artist(self):
        self.client.login(username='mandy_admin', password='password')
        url = '/music/artist/'
        data = {
            'name': 'New Artist',
            'genre': 'Rock',
            'popularity': 2,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_artist(self):
        self.client.login(username='mandy_admin', password='password')  # login before the request
        url = f'/music/artist/{self.artist.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_artist(self):
        self.client.login(username='mandy_admin', password='password')
        url = f'/music/artist/{self.artist.id}/'
        data = {
            'name': 'Updated Artist',
            'genre': self.artist.genre,
            'popularity': self.artist.popularity,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_artist(self):
        self.client.login(username='mandy_admin', password='password')
        url = f'/music/artist/{self.artist.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_artist_by_genre(self):
        self.client.login(username='mandy_admin', password='password')
        url = f'/music/artist/genre/{self.artist.genre}/'        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_albums_by_artist(self):
        self.client.login(username='mandy_admin', password='password')
        url = f'/music/artist/{self.artist.id}/albums/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_popular_artists(self):
        self.client.login(username='mandy_admin', password='password')
        url = '/music/artists/popular/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




class AlbumTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='password', email='admin@example.com')
        self.artist = Artist.objects.create(name='Artist', genre='Genre', popularity=1)
        self.album = Album.objects.create(title='Album', release_date='2000-01-01', artist=self.artist)  # remove 'genre'

    def test_create_album(self):
        self.client.login(username='admin', password='password')
        url = '/music/album/'
        data = {'title': 'New Album', 'release_date': '2001-01-01', 'artist': self.artist.id}  # remove 'genre'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_album(self):
        self.client.login(username='admin', password='password')  # add this line
        url = f'/music/album/{self.album.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_album(self):
        self.client.login(username='admin', password='password')
        url = f'/music/album/{self.album.id}/'
        data = {
        'title': 'Updated Album',
        'release_date': self.album.release_date,  # use release_date directly
        'artist': self.album.artist.id,
        # add any other fields required by your API
    }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # print the error message if the request fails


    def test_delete_album(self):
        self.client.login(username='admin', password='password')
        url = f'/music/album/{self.album.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_latest_album_by_artist(self):
        self.client.login(username='admin', password='password')  # login before the request
        url = f'/music/artist/{self.artist.id}/latest_album/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_popular_albums(self):
        self.client.login(username='admin', password='password')  # login before the request
        url = '/music/albums/popular/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)