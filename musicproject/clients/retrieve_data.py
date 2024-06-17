import requests
from getpass import getpass

BASE_URL = 'http://127.0.0.1:8000/'
URL_AUTH = f'{BASE_URL}auth/'

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

# GET a los artistas por género
url = f'{BASE_URL}music/artist/genre/Rock/'  
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Artistas por género:', response.json())
else:
    print('Error:', response.status_code)


# GET a los artistas más populares
url = f'{BASE_URL}music/artists/popular/'  
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Artistas más populares:', response.json())
else:
    print('Error:', response.status_code)

# GET a los álbumes por artista
url = f'{BASE_URL}music/artist/1/albums/' 
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Álbumes por artista:', response.json())
else:
    print('Error:', response.status_code)

# GET a los álbumes más populares

url = f'{BASE_URL}music/albums/popular/' 
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Álbumes más populares:', response.json())
else:
    print('Error:', response.status_code)

# GET al álbum más reciente de un artista
url = f'{BASE_URL}music/artist/1/album/recent/'  
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('Álbum más reciente del artista:', response.json())
else:
    print('Error:', response.status_code)
