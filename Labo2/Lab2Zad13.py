slownik1 = ({"Andrzej": ("Kowalski", 22),
         "Tomasz": ("Nowak", 20),
         "Zbigniew": ("Kiepa", 21),
         "Marta": ("Pieczewska", 19),
         })

slownik2 = ({"Henryk": ("Pika", 68),
         "Lorem": ("Ipsum", 20),
         "Kek": ("Peepo", 21),
         "xyz": ("XAE-12", 1),
         })

lista = [slownik1, slownik2]

for i in lista:
    for j in i.values():
        for k in j:
            print(str(k), end=' ')
        print(" ")