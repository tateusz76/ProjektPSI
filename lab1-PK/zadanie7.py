lista = list(range(1, 11))
print(lista)
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
lista.extend(lista2)
print(lista)
lista3 = [0]
lista3.extend(lista)
print(lista3)
list_c = lista3
list_c.sort(reverse=True)
print(list_c)