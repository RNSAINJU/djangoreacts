from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import generics

class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer