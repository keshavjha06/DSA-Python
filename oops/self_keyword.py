class Car:
    def __init__(self, price=0, name=None):
        self.price = price  # self.price is the object's field, price is the parameter
        self.name = name

    def print(self):
        price = 12  # local variable; self.price still gives the object's price
        print(self.price, self.name)


c1 = Car(1250000, "Kia Sonnet")
c1.print()
c2 = Car(name="Lord Altos", price=400000)
c2.print()
c3 = Car()
c3.name = "Honda Amaze"
