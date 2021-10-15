import math

#Zadanie 6
print("Zadanie 6")
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

srodek = len(lista)//2

listaA = lista[:srodek]
print(listaA)

listaB = lista[srodek:]
print(listaB)

#Zadanie 7
print("Zadanie 7")
listaMerge = listaA + listaB
print(listaMerge)