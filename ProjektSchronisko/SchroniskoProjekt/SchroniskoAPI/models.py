from django.db import models

# Create your models here.

# Stanowiska = [
#     ("chirug", "chirurg"),
#     ("wolontariusz", "wolontariusz"),
#     ("pracownik administracji", "pracownik administracji"),
#     ("pracownik konserwacji", "pracownik konserwacji"),
# ]
#
# Zabiegi = [
#     ("operacja", "operacja"),
#     ("szczepienie", "szczepienie"),
#     ("okresowe badanie", "okresowe badanie"),
# ]


class Stanowisko(models.Model):
    stanowisko = models.CharField(max_length=45)
    owner = models.ForeignKey('auth.User', related_name='stanowiskaUser', on_delete=models.CASCADE)

    def __str__(self):
        name = str(self.stanowisko)
        return name

    class Meta:
        verbose_name_plural = "Stanowiska"


class RodzajeZabiegow(models.Model):
    rodzaj = models.CharField(max_length=45)
    owner = models.ForeignKey('auth.User', related_name='zabiegiUser', on_delete=models.CASCADE)

    def __str__(self):
        name = str(self.rodzaj)
        return name

    class Meta:
        verbose_name_plural = "Rodzaje Zabiegów"


class Adopcja(models.Model):
    dataAdopcji = models.DateField()
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)

    def __str__(self):
        name = str(self.dataAdopcji)
        return name

    class Meta:
        verbose_name_plural = "Adopcje"


class Zwierze(models.Model):
    data_adopcji = models.ForeignKey(Adopcja, related_name='adopcje', on_delete=models.CASCADE, null=True, blank=True)
    imie = models.CharField(max_length=30)
    rasa = models.CharField(max_length=30)
    rok_Urodzenia = models.IntegerField()
    rok_Przygarniecia = models.IntegerField()
    kot = models.BooleanField()

    def __str__(self):
        if not self.kot:
            gatunek = 'pies'
        else:
            gatunek = 'kot'
        return self.imie + ' | ' + gatunek

    class Meta:
        verbose_name_plural = "Zwierzęta"


class Pracownik(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    dataZatrudnienia = models.DateField()
    stanowisko = models.ForeignKey(Stanowisko, related_name='stanowiska', on_delete=models.CASCADE)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko + ' | ' + str(self.stanowisko)

    class Meta:
        verbose_name_plural = "Pracownicy"


class Zabieg(models.Model):
    zwierze = models.ForeignKey(Zwierze, related_name='zabieg', on_delete=models.CASCADE)
    rodzajZabiegu = models.ForeignKey(RodzajeZabiegow, related_name='rodzaje', on_delete=models.CASCADE)
    dataZabiegu = models.DateField(null=True)
    pracownicy = models.ManyToManyField('pracownik')

    def __str__(self):
        # rodzaj = str(self.rodzajZabiegu)
        # data = str(self.dataZabiegu)
        # name = rodzaj + ' | ' + data
        return ''

    class Meta:
        verbose_name_plural = "Zabiegi"
