def przelicz(type, temp):
    if type == 1:
        temp = (9/5 * temp) + 32

    if type == 2:
        temp = (temp + 273.15) * 9/5

    if type == 3:
        temp = temp + 273.15

    return temp

print(przelicz(1,23))
print(przelicz(2,23))
print(przelicz(3,23))