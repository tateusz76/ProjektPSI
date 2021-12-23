from .models import Adopcja
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class StanowiskoList(generics.ListAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer


class RodzajeList(generics.ListAPIView):
    queryset = RodzajeZabiegow.objects.all()
    serializer_class = RodzajeSerializer
    name = 'rodzaje-list'


class RodzajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RodzajeZabiegow.objects.all()
    serializers_class = RodzajeSerializer
    view_name = 'rodzaje-details'


class AdopcjaList(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class AdopcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer


class ZwierzeList(generics.ListCreateAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer
    name = 'zwierze-list'


class ZwierzeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer
    name = 'zwierze-details'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer


class ZabiegiList(generics.ListCreateAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer
    name = 'zabieg-list'


class ZabiegiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zabieg.objects.all()
    serializer_class = ZabiegiSerializer
    name = 'zabieg-details'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'zwierzeta': reverse(ZwierzeList.name, request=request),
                         'adopcje': reverse(AdopcjaList.name, request=request),
                         'pracownicy': reverse(PracownikList.name, request=request),
                         'zabiegi': reverse(ZabiegiList.name, request=request),
                         'rodzajezabiegow': reverse(RodzajeList.name, request=request),
                         'stanowiska': reverse(StanowiskoList.name, request=request)
                         })
