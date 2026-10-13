class Car:
    def __init__(self):
        self.seats = 0
        self.name = None
        self.length = 0.0
        self.type = None
        self.torque = 0

    def print(self):
        print(self.seats, self.name, self.length, self.type, self.torque)


def change(x):
    # x refers to the same object, so the change is visible outside
    x.seats = 4


c = Car()
c.length = 3.99
c.name = "Kia Sonnet"
c.seats = 5
c.type = "SUV"
c.torque = 100

change(c)

print(c.seats)

c.print()
