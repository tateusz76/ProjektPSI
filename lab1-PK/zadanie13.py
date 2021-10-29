dict1 = ({123456: ("student numer1", 19, "email1@a.com", 1999, "adres1"),
         789101: ("student numer2", 20, "email2@a.com", 1999, "adres2"),
         415161: ("student numer3", 21, "email3@a.com", 1999, "adres3"),
         718192: ("student numer3", 19, "email4@a.com", 1999, "adres4"),
         })

dict2 = ({123456: ("student numer4", 21, "email4@a.com", 1999, "adres5"),
         789101: ("student numer5", 22, "email5@a.com", 1999, "adres6"),
         415161: ("student numer6", 23, "email6@a.com", 1999, "adres7"),
         718192: ("student numer7", 24, "email7@a.com", 1999, "adres8"),
         })

lista = [dict1, dict2]
for x in lista:
    for y in x.values():
        for z in y:
            print(str(z), end='')
        print("\n")