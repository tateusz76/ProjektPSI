imie = "Piotr"
nazwisko = "Kowalski"
formulka = f"Nazywam się {imie} {nazwisko}"

print('{:>60}'.format(formulka))
print('{:|>40}'.format(formulka))
print('{:.7}s'.format(formulka))
print('{:>10.7}s'.format(formulka))

data = {'first' : imie, 'last' : nazwisko}
print('{first} {last}'.format(**data))