class Car:
    # default arguments replace the separate default constructor
    def __init__(self, seats=0, name=None, length=0.0):
        self.seats = seats
        self.name = name
        self.length = length

    def print(self):
        print(self.seats, self.name, self.length)


c1 = Car(4, "Kia", 3.99)
c1.print()
c2 = Car(5, "Altos", 3.75)
c2.print()
c3 = Car()
c3.name = "Honda Amaze"
