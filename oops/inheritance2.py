# Method overriding (runtime polymorphism):
# a subclass provides its own version of the parent's method.
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Lion(Animal):
    def sound(self):
        print("Lion Roars")


a = Dog()
b = Lion()
a.sound()
b.sound()
