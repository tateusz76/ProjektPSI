from .models import Adopcja
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from django.contrib.auth.models import User
from .custompermission import OwnerOrRead


class StanowiskoList(generics.ListCreateAPIView):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer
    name = 'stanowisko-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, OwnerOrRead,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RodzajeList(generics.ListAPIView):
    queryset = RodzajeZabiegow.objects.all()
    serializer_class = RodzajeSerializer
    name = 'rodzaje-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, OwnerOrRead,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RodzajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RodzajeZabiegow.objects.all()
    serializers_class = RodzajeSerializer
    view_name = 'rodzaje-details'


class AdopcjaList(generics.ListCreateAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    name = 'adopcja-list'


class AdopcjaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adopcja.objects.all()
    serializer_class = AdopcjaSerializer
    name = 'adopcja-details'


class ZwierzeList(generics.ListCreateAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer
    name = 'zwierze-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    search_fields = ['imie']


class ZwierzeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zwierze.objects.all()
    serializer_class = ZwierzeSerializer
    name = 'zwierze-details'


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-list'


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-details'


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
