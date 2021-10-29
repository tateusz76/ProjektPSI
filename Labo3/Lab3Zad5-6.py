class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


    def difference(self):
        return self.a - self.b


    def multiply(self):
        return self.a * self.b


    def divide(self):
        return self.a / self.b

class ScienceCalculator(Calculator):
    def power(self):
        return self.a ** self.b

    def rest(self):
        return self.a % self.b


a = int(input("Podaj liczbę 1:"))
b = int(input("Podaj liczbę 2:"))
obj = Calculator(a, b)
obj2 = ScienceCalculator(a, b)

print(obj2.power())


