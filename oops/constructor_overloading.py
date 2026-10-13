# Python has no constructor overloading. Default arguments cover the empty
# constructor, and keyword arguments let the caller pass values in any order.
class Car:
    def __init__(self, price=0, name=None):
        self.price = price
        self.name = name

    def print(self):
        print(self.price, self.name)


c1 = Car(1250000, "Kia")
c1.print()
c2 = Car(name="Altos", price=400000)
c2.print()
c3 = Car()
c3.name = "Honda Amaze"
