from .models import Adopcja
from .serializers import *
from rest_framework import generics


class AdopcjaList(generics.ListAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class AdopcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class ZwierzeList(generics.ListAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer


class ZwierzeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer


class PracownikList(generics.ListAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class ZabiegiList(generics.ListAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer


class ZabiegiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer
