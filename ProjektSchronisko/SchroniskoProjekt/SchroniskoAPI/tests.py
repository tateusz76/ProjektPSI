import datetime
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import *
from django import urls
from django.contrib.auth.models import User
from rest_framework import status


class AdopcjaTests(APITestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def post_adopcja(self, dataAdopcji, imie, nazwisko):
        url = reverse(views.AdopcjaList.name)
        data = {'dataAdopcji': dataAdopcji,
                'imie': imie,
                'nazwisko': nazwisko}
        response = self.client.post(url, data, format='json')
        print(response)
        return response

    def test_post_and_get_adopcja(self):
        data = datetime.date(2022, 1, 1)
        response = self.post_adopcja(data, 'Maciek', 'Adopcjusz')
        print(response)
        assert response.status_code == status.HTTP_201_CREATED
        assert Adopcja.objects.count() == 1
        assert Adopcja.objects.get().imie == 'Maciek'

    def test_update_adopcja(self):
        date = datetime.date(2022, 1, 1)
        response = self.post_adopcja(date, 'Maciek', 'Adopcjusz')
        url = urls.reverse(views.AdopcjaDetail.name, None, {response.data['id']})
        new_date = datetime.date(2022, 2, 13)
        data = {'dataAdopcji': new_date,
                'imie': 'Maciek',
                'nazwisko': 'Adopcjusz'}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['dataAdopcji'] == '2022-02-13'


class PracownikTests(APITestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def post_stanowisko(self, stanowisko):
        url = reverse(views.StanowiskoList.name)
        data = {'stanowisko': stanowisko}
        response = self.client.post(url, data, format='json')
        print(response)
        return response

    def test_post_and_get_stanowisko(self):
        response = self.post_stanowisko('stanowiskotest')
        print(response)
        assert response.status_code == status.HTTP_201_CREATED
        assert Stanowisko.objects.count() == 1
        assert Stanowisko.objects.get().stanowisko == 'stanowiskotest'

    def post_pracownik(self, imie, nazwisko, dataZatrudnienia, stanowisko):
        url = reverse(views.PracownikList.name)
        data = {"imie": imie,
                "nazwisko": nazwisko,
                "dataZatrudnienia": dataZatrudnienia,
                "stanowisko": stanowisko}
        response = self.client.post(url, data, format='json')
        print(response)
        return response

    def test_post_and_get_pracownik(self):
        self.post_stanowisko('wolontariusz')
        response = self.post_pracownik('Test', 'Test', '2021-12-04', 'wolontariusz')
        print(response)
        assert response.status_code == status.HTTP_201_CREATED
        assert Pracownik.objects.count() == 1
        assert Pracownik.objects.get().imie == 'Test'

    def test_update_pracownik(self):
        self.post_stanowisko('wolontariusz')
        response = self.post_pracownik('Test', 'Test', '2021-12-04', 'wolontariusz')
        url = urls.reverse(views.PracownikDetail.name, None, {response.data['id']})
        new_name = 'TestUpdated'
        data = {'imie': new_name,
                'nazwisko': 'Adopcjusz',
                'dataZatrudnienia':'2021-12-04',
                'stanowisko': 'wolontariusz'}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['imie'] == new_name


class ZwierzeTests(APITestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def create_adopcja(self, dataAdopcji, imie, nazwisko):
        url = reverse(views.AdopcjaList.name)
        data = {'dataAdopcji': dataAdopcji,
                'imie': imie,
                'nazwisko': nazwisko}
        response = self.client.post(url, data, format='json')
        print(response)
        return response

    def post_zwierze(self, data_adopcji, imie, rasa, rok_Urodzenia, rok_Przygarniecia, kot):
        url = reverse(views.ZwierzeList.name)
        data = {"data_adopcji": data_adopcji,
                "imie": imie,
                "rasa": rasa,
                "rok_Urodzenia": rok_Urodzenia,
                "rok_Przygarniecia": rok_Przygarniecia,
                "kot": kot}
        response = self.client.post(url, data, format='json')
        print(response)
        return response

    def test_post_and_get_zwierze(self):
        data = datetime.date(2022, 1, 1)
        self.create_adopcja(data, 'Maciek', 'Adopcjusz')
        response = self.post_zwierze('2022-01-01', 'Test', 'Test', 2007, 2013, True)
        print(response)
        assert response.status_code == status.HTTP_201_CREATED
        assert Zwierze.objects.count() == 1
        assert Zwierze.objects.get().imie == 'Test'

    def test_update_pracownik(self):
        data = datetime.date(2022, 1, 1)
        self.create_adopcja(data, 'Maciek', 'Adopcjusz')
        response = self.post_zwierze('2022-01-01', 'Test', 'Test', 2007, 2013, True)
        url = urls.reverse(views.ZwierzeDetail.name, None, {response.data['id']})
        new_name = 'TestUpdated'
        data = {"data_adopcji": '2022-01-01',
                "imie": new_name,
                "rasa": 'Test',
                "rok_Urodzenia": 2007,
                "rok_Przygarniecia": 2013,
                "kot": True}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['imie'] == new_name
