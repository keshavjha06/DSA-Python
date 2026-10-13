class Dog:
    def speak(self):
        print("Bhau Bhau")


class Cat:
    def speak(self):
        print("Meow Meow")


class Lion:
    def speak(self):
        print("GRRRRRR")


class Pikachu:
    def speak(self):
        print("Pika Pika")


class Human:
    def speak(self):
        print("Hello")


# Python has no method overloading; a default argument handles 2 or 3 numbers
def find_max(a, b, c=None):
    if c is None:
        return max(a, b)
    return max(a, max(b, c))


h = Human()
c = Cat()
p = Pikachu()
d = Dog()
l = Lion()

d.speak()
l.speak()
h.speak()
c.speak()
p.speak()
print(find_max(4, 5, 6))
