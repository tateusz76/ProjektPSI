from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class AdopcjaSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='adopcja-detail', read_only=True)
    class Meta:
        model = Adopcja
        fields = ['id', 'dataAdopcji', 'imie', 'nazwisko']


class ZwierzeSerializer(serializers.HyperlinkedModelSerializer):
    id_adopcji = serializers.SlugRelatedField(queryset=Adopcja.objects.all(), slug_field='id', required=False)
    zabieg = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zabieg-details')
    url = serializers.HyperlinkedIdentityField(view_name='zwierze-details', read_only=True)

    class Meta:
        model = Zwierze
        fields = ['id', 'url', 'id_adopcji', 'imie', 'rasa', 'rok_Urodzenia', 'rok_Przygarniecia', 'kot', 'zabieg']


class PracownikSerializer(serializers.HyperlinkedModelSerializer):
    stanowisko = serializers.SlugRelatedField(queryset=Stanowisko.objects.all(), slug_field='stanowisko')
    url = serializers.HyperlinkedIdentityField(view_name='pracownik-details', read_only=True)

    class Meta:
        model = Pracownik
        fields = ['id', 'url', 'imie', 'nazwisko', 'dataZatrudnienia', 'stanowisko']


class StanowiskoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'stanowisko']


class RodzajeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RodzajeZabiegow
        fields = ['id', 'rodzaj']


class ZabiegiSerializer(serializers.HyperlinkedModelSerializer):
    rodzajZabiegu = serializers.SlugRelatedField(queryset=RodzajeZabiegow.objects.all(), slug_field='rodzaj')
    zwierze = serializers.SlugRelatedField(queryset=Zwierze.objects.all(), slug_field='imie')
    pracownicy = serializers.SlugRelatedField(queryset=Pracownik.objects.all(), many=True, slug_field='imie')
    url = serializers.HyperlinkedIdentityField(view_name='zabieg-details', read_only=True)

    class Meta:
        model = Zabieg
        fields = ['id', 'url', 'zwierze', 'rodzajZabiegu', 'dataZabiegu', 'pracownicy']
