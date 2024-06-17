from rest_framework import generics
from .models import Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets



#Vistas genéricas para Artist


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class ArtistRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    

class ArtistByGenreList(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Artist.objects.filter(genre=genre)
    
class PopularArtistsList(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        return Artist.objects.order_by('popularity')[:5]  # top 5 artistas más populares

#Vistas genéricas para Album

class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class AlbumRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    

class AlbumByArtistList(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        artist_id = self.kwargs['artist_id']
        return Album.objects.filter(artist__id=artist_id)
    
class PopularAlbumsList(generics.ListAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.order_by('popularity')[:5]  # top 5 álbumes más populares
    

@api_view(['GET'])
@permission_classes([AllowAny])
def latest_album_by_artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    latest_album = artist.album_set.order_by('release_date').first()
    serializer = AlbumSerializer(latest_album)
    return Response(serializer.data)