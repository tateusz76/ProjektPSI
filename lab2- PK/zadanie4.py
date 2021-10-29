def funkcja4(type, temp):
    if type == 1:
        F = temp * 1.8 + 32
        print(F)
    elif type == 2:
        K = (F + 459.67) / 1.8
        print(K)
    elif type == 3: #kelvin
        Ra = F + 459.67
        print(Ra)

funkcja4(1, 32)