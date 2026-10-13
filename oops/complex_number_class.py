class ComplexNumber:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print(self):
        if self.y >= 0:
            print(f"{self.x} + {self.y}i")
        else:
            print(f"{self.x} - {-self.y}i")

    def add(self, z):
        self.x = self.x + z.x
        self.y = self.y + z.y

    def multiply(self, z):
        new_x = self.x * z.x - self.y * z.y  # temp variables
        new_y = self.x * z.y + self.y * z.x
        self.x = new_x
        self.y = new_y

    def divide(self, z):
        denom = z.x * z.x + z.y * z.y
        # int(a / b) truncates toward zero like Java's int division
        new_x = int((self.x * z.x + self.y * z.y) / denom)
        new_y = int((self.y * z.x - self.x * z.y) / denom)
        self.x = new_x
        self.y = new_y


z1 = ComplexNumber(2, -5)
z2 = ComplexNumber(3, 4)
z1.print()
z2.print()
z1.add(z2)
z1.print()
z2.print()
z2.multiply(z1)
z1.print()
z2.print()
z2.divide(z1)
z1.print()
z2.print()
