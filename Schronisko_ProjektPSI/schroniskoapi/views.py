from django.shortcuts import render
from rest_framework import viewsets
from . import models
#from . import serializers

# class ZwierzeViewset(viewsets.ModelViewSet):
#     queryset = models.Zwierze.objects.all()
#     serializer_class = serializers.ZwierzeSerializer
#
# class PracownikViewset(viewsets.ModelViewSet):
#     queryset = models.Pracownik.objects.all()
#     serializer_class = serializers.PracownikSerializer
#
# class ZabiegViewset(viewsets.ModelViewSet):
#     queryset = models.Zabieg.objects.all()
#     serializer_class = serializers.ZabiegSerializer
#
# class MagazynViewset(viewsets.ModelViewSet):
#     queryset = models.Magazyn.objects.all()
#     serializer_class = serializers.MagazynSerializer
#
# class DatkiViewset(viewsets.ModelViewSet):
#     queryset = models.Datki.objects.all()
#     serializer_class = serializers.DatkiSerializer
#
# class ZamowieniaViewset(viewsets.ModelViewSet):
#     queryset = models.Zamowienia.objects.all()
#     serializer_class = serializers.ZamowieniaSerializer
