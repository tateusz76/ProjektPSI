from .models import Adopcja
from .serializers import *
from rest_framework import generics


class StanowiskoList(generics.ListAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer


class RodzajeList(generics.ListAPIView):
    queryset = RodzajeZabiegow.objects.all()
    serializer_class = RodzajeSerializer


class AdopcjaList(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class AdopcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class ZwierzeList(generics.ListCreateAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer


class ZwierzeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class ZabiegiList(generics.ListCreateAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer


class ZabiegiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer
