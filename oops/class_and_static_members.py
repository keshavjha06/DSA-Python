class Cricketer:
    # class variable: shared by all objects (like Java's static)
    country = "NZ"
    # Python has no final; constants are written in UPPER_CASE by convention

    def __init__(self):
        self.runs = 0
        self.name = None
        self.avg = 0.0

    def print(self):
        print(self.runs, self.name, self.avg)

    @staticmethod
    def greet():
        print(" I only believe in Jassi Bhai")


Cricketer.greet()
print(Cricketer.country)
