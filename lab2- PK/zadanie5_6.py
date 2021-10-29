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
        return self.a - self.b


class ScienceCalculator(Calculator):
    def modulo(self):
        return self.a % self.b

    def pow(self):
        return self.a ** self.b


Calc = Calculator(5, 8)
print(Calc.add())
S_Calc = ScienceCalculator(5, 2)
print(S_Calc.pow())