from django.db import models

# Create your models here.

Stanowiska = [
    ("chirug", "chirurg"),
    ("wolontariusz", "wolontariusz"),
    ("pracownik administracji", "pracownik administracji"),
    ("pracownik konserwacji", "pracownik konserwacji"),
]

Zabiegi = [
    ("operacja", "operacja"),
    ("szczepienie", "szczepienie"),
    ("okresowe badanie", "okresowe badanie"),
]


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
    idAdopcja = models.ForeignKey(Adopcja, related_name='adopcje', on_delete=models.CASCADE, null=True, blank=True)
    imie = models.CharField(max_length=30)
    rasa = models.CharField(max_length=30)
    rokUrodzenia = models.IntegerField()
    rokPrzygarniecia = models.IntegerField()
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
    stanowisko = models.CharField(max_length=45, choices=Stanowiska)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko + ' | ' + self.stanowisko

    class Meta:
        verbose_name_plural = "Pracownicy"


class Zabieg(models.Model):
    idZwierze = models.ForeignKey(Zwierze, related_name='zwierze', on_delete=models.CASCADE)
    rodzajZabiegu = models.CharField(max_length=45, choices=Zabiegi)
    dataZabiegu = models.DateField(null=True)
    pracownicy = models.ManyToManyField('pracownik')

    def __str__(self):
        rodzaj = str(self.rodzajZabiegu)
        data = str(self.dataZabiegu)
        name = rodzaj + ' | ' + data
        return name

    class Meta:
        verbose_name_plural = "Zabiegi"
