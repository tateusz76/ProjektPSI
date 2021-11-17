from django.db import models


# Create your models here.


class Zwierze(models.Model):
    imie = models.TextField()
    rasa = models.TextField()
    rokUrodzenia = models.IntegerField()
    rokPrzygarniecia = models.IntegerField()
    typ = models.IntegerField()


class pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    dataZatrudnienia = models.DateField()
    stanowisko = models.CharField(max_length=45)


class zabieg(models.Model):
    idZwierze = models.ForeignKey(Zwierze, on_delete=models.CASCADE)
    rodzajZabiegu = models.CharField(max_length=45)
    pracownicy = models.ManyToManyField('pracownik')


class magazyn(models.Model):
    nazwaObiektu = models.CharField(max_length=45)
    ilosc = models.IntegerField()


class datki(models.Model):
    nazwa = models.CharField(max_length=45)
    ilosc = models.IntegerField()
    idObiektu = models.ForeignKey(magazyn, on_delete=models.CASCADE)


class zamowienia(models.Model):
    nazwaObiektu = models.CharField(max_length=45)
    ilosc = models.IntegerField()
    dataZamowienia = models.DateField()
    idObiektu = models.ForeignKey(magazyn, on_delete=models.CASCADE)
