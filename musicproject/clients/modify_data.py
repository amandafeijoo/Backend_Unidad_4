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
if response.status_code == 200:
    token = response.json()['token']
else:
    print(f'Error al obtener token: {response.status_code} {response.text}')
    exit(1)

headers = {'Authorization': f'Token {token}'}

# actualizar  artista
def update_artist(artist_id, new_data):
    url = f'{URL_ARTIST}{artist_id}/'  
    response = requests.put(url, headers=headers, data=new_data)
    if response.status_code == 200:
        print('Artista actualizado:', response.json())
    else:
        print('Error al actualizar el artista:', response.status_code)

#  eliminar un artista
def delete_artist(artist_id):
    url = f'{URL_ARTIST}{artist_id}/'  
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:  
        print('Artista eliminado con éxito')
    else:
        print('Error al eliminar el artista:', response.status_code)

# actualizar un álbum
def update_album(album_id, new_data):
    url = f'{URL_ALBUM}{album_id}/'  
    response = requests.put(url, headers=headers, data=new_data)
    if response.status_code == 200:
        print('Álbum actualizado:', response.json())
    else:
        print('Error al actualizar el álbum:', response.status_code)

# eliminar un álbum
def delete_album(album_id):
    url = f'{URL_ALBUM}{album_id}/'  
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:  
        print('Álbum eliminado con éxito')
    else:
        print('Error al eliminar el álbum:', response.status_code)
        
# Ejemplo de uso
update_artist(1, {'name': 'Empire Of The Sun', 'genre': 'Rock', 'popularity': 5})
update_album(1, {'title': 'In the rainbow', 'artist': 1, 'release_date': '2008-08-30', 'popularity': 3})