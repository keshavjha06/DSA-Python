class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        self.simplify()

    def print(self):
        print(f"{self.num}/{self.denom}")

    def add(self, f):
        self.num = self.num * f.denom + self.denom * f.num
        self.denom = self.denom * f.denom
        self.simplify()

    def multiply(self, f):
        self.num = self.num * f.num
        self.denom = self.denom * f.denom
        self.simplify()

    def divide(self, f):
        self.num = self.num * f.denom
        self.denom = self.denom * f.num
        self.simplify()

    def simplify(self):
        is_negative = self.num * self.denom < 0
        self.num = abs(self.num)
        self.denom = abs(self.denom)
        gcd = self.hcf(self.num, self.denom)
        self.num = self.num // gcd
        self.denom = self.denom // gcd
        if is_negative:
            self.num = -self.num

    def hcf(self, a, b):
        if a == 0:
            return b
        return self.hcf(b % a, a)


f1 = Fraction(3, -7)
f2 = Fraction(7, 3)
f1.multiply(f2)
f1.print()
f3 = Fraction(-50, -100)
f3.print()
