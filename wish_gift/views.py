from rest_framework import generics
from .serializers import ListSerializer
from .models import List

class ListList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

