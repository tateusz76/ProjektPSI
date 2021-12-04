from rest_framework import serializers
from .models import *


class AdopcjaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dataAdopcji = serializers.DateField(required=True)
    imie = serializers.CharField(required=True, max_length=30)
    nazwisko = serializers.CharField(required=True, max_length=30)

    def create(self, validated_data):
        return Adopcja.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dataAdopcji = validated_data.get('dataAdopcji', instance.dataAdopcji)
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.save()
        return instance


class ZwierzeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    idAdopcja = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='adopcja_list')
    imie = serializers.CharField(required=True, max_length=30)
    rasa = serializers.CharField(required=True, max_length=30)
    rokUrodzenia = serializers.IntegerField(required=True)
    rokPrzygarniecia = serializers.IntegerField(required=True, )
    kot = serializers.BooleanField(required=True)

    def create(self, validated_data):
        return Zwierze.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idAdopcja = validated_data.get('dataAdopcji', instance.dataAdopcji)
        instance.imie = validated_data.get('imie', instance.imie)
        instance.rasa = validated_data.get('rasa', instance.rasa)
        instance.rokUrodzenia = validated_data.get('rokUrodzenia', instance.rokUrodzenia)
        instance.rokPrzygarniecia = validated_data.get('rokPrzygarniecia', instance.rokPrzygarniecia)
        instance.kot = validated_data.get('kot', instance.kot)
        instance.save()
        return instance


class PracownikSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True, max_length=45)
    nazwisko = serializers.CharField(required=True, max_length=45)
    dataZatrudnienia = serializers.DateField(required=True)
    stanowisko = serializers.CharField(required=True, max_length=45)

    def create(self, validated_data):
        return Pracownik.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.dataZatrudnienia = validated_data.get('dataZatrudnienia', instance.dataZatrudnienia)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance


class ZabiegiSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    idZwierze = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zwierze_list')
    rodzajZabiegu = serializers.CharField(required=True, max_length=45)
    dataZabiegu = serializers.DateField(required=True)
    pracownicy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='pracownik_list')

    def create(self, validated_data):
        return Zabiegi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.idZwierze = validated_data.get('idZwierze', instance.idZwierze)
        instance.rodzajZabiegu = validated_data.get('rodzajZabiegu', instance.rodzajZabiegu)
        instance.dataZabiegu = validated_data.get('dataZabiegu', instance.dataZabiegu)
        instance.pracownicy = validated_data.get('pracownicy', instance.pracownicy)
