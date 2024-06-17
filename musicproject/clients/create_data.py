import requests
from getpass import getpass

BASE_URL = 'http://127.0.0.1:8000/'
URL_AUTH = f'{BASE_URL}auth/'
URL_ARTIST = f'{BASE_URL}music/artist/'
URL_ALBUM = f'{BASE_URL}music/album/'

username = input('Usuario: ')
password = getpass('Contrasena: ')

auth_data = {'username': username, 'password': password}
response = requests.post(URL_AUTH, data=auth_data)
print(response.json())  # Imprime la respuesta completa
if response.status_code == 200:
    token = response.json()['token']
    print(f'Token: {token}')  # Imprime el token
else:
    print(f'Error al obtener token: {response.status_code} {response.text}')
    exit(1)

headers = {'Authorization': f'Token {token}'}

#ejemplo de creación de datos
artists = [
    {'name': 'Onda Vaga', 'genre': 'Rumba', 'popularity': 5},
]

albums = [
    {'title': 'Fuerte y Caliente', 'artist': 'Onda Vaga', 'release_date': '2008-10-10', 'popularity': 1 },
]

artist_ids = {}
album_ids = {}

for artist in artists:
    response = requests.post(URL_ARTIST, headers=headers, data=artist)
    if response.status_code == 201:
        artist_id = response.json()['id']
        artist_ids[artist['name']] = artist_id
        print(f'Artista creado: {artist["name"]} (ID: {artist_id})')
    else:
        print(f'Error al crear artista: {response.status_code} {response.text}')

for album in albums:
    artist_name = album['artist']
    if artist_name in artist_ids:
        album['artist'] = artist_ids[artist_name]
        response = requests.post(URL_ALBUM, headers=headers, data=album)
        if response.status_code == 201:
            album_id = response.json()['id']
            album_ids[album['title']] = album_id
            print(f'Álbum creado: {album["title"]} (ID: {album_id})')
        else:
            print(f'Error al crear álbum: {response.status_code} {response.text}')