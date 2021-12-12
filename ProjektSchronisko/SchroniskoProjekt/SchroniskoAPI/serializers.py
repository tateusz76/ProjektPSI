from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class AdopcjaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adopcja
        fields = ['id', 'dataAdopcji', 'imie', 'nazwisko']


class ZwierzeSerializer(serializers.HyperlinkedModelSerializer):
    data_adopcji = serializers.SlugRelatedField(queryset=Adopcja.objects.all(), slug_field='dataAdopcji')

    class Meta:
        model = Zwierze
        fields = ['id', 'data_adopcji', 'imie', 'rasa', 'rok_Urodzenia', 'rok_Przygarniecia', 'kot']


class PracownikSerializer(serializers.HyperlinkedModelSerializer):
    stanowisko = serializers.SlugRelatedField(queryset=Stanowisko.objects.all(), slug_field='stanowisko')

    class Meta:
        model = Pracownik
        fields = ['id', 'imie', 'nazwisko', 'dataZatrudnienia', 'stanowisko']


class StanowiskoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'stanowisko']


class RodzajeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RodzajeZabiegow
        fields = ['id', 'rodzaj']


class ZabiegiSerializer(serializers.HyperlinkedModelSerializer):
    rodzajZabiegu = serializers.SlugRelatedField(queryset=RodzajeZabiegow.objects.all(), slug_field='rodzaje')
    idZwierze = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zwierze_details')
    # pracownicy = serializers.SlugRelatedField(queryset=Pracownik.objects.all(), slug_field='imie')

    class Meta:
        model = Zabieg
        fields = ['id', 'rodzajZabiegu', 'idZwierze', 'dataZabiegu']

