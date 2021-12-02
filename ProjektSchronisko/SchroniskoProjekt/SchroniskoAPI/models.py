from django.db import models


# Create your models here.

class Adopcja(models.Model):
    dataAdopcji = models.DateField()
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)


class Zwierze(models.Model):
    idAdopcja = models.ForeignKey(Adopcja, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=30)
    rasa = models.CharField(max_length=30)
    rokUrodzenia = models.IntegerField()
    rokPrzygarniecia = models.IntegerField()
    typ = models.IntegerField()


class Pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    dataZatrudnienia = models.DateField()
    stanowisko = models.CharField(max_length=45)


class Zabieg(models.Model):
    idZwierze = models.ForeignKey(Zwierze, on_delete=models.CASCADE)
    rodzajZabiegu = models.CharField(max_length=45)
    pracownicy = models.ManyToManyField('pracownik')



