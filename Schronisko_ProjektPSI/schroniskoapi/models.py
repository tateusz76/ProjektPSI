from django.db import models

# Create your models here.

class Zwierze(models.Model):
   imie = models.CharField(max_length=30)
   rasa = models.CharField(max_length=30)
   rokUrodzenia = models.IntegerField()
   rokPrzygarniecia = models.IntegerField()
   typ = models.IntegerField()

# class Zwierze(models.Model):
#     imie = models.CharField()
#     rasa = models.CharField()
#     rokUrodzenia = models.IntegerField()
#     rokPrzygarniecia = models.IntegerField()
#     typ = models.IntegerField()
#
#
# class Pracownik(models.Model):
#     imie = models.CharField(max_length=45)
#     nazwisko = models.CharField(max_length=45)
#     dataZatrudnienia = models.DateField()
#     stanowisko = models.CharField(max_length=45)
#
#
# class Zabieg(models.Model):
#     idZwierze = models.ForeignKey(Zwierze, on_delete=models.CASCADE)
#     rodzajZabiegu = models.CharField(max_length=45)
#     pracownicy = models.ManyToManyField('pracownik')
#
#
# class Magazyn(models.Model):
#     nazwaObiektu = models.CharField(max_length=45)
#     ilosc = models.IntegerField()
#
#
# class Datki(models.Model):
#     nazwa = models.CharField(max_length=45)
#     ilosc = models.IntegerField()
#     idObiektu = models.ForeignKey(magazyn, on_delete=models.CASCADE)
#
#
# class Zamowienia(models.Model):
#     nazwaObiektu = models.CharField(max_length=45)
#     ilosc = models.IntegerField()
#     dataZamowienia = models.DateField()
#     idObiektu = models.ForeignKey(magazyn, on_delete=models.CASCADE)