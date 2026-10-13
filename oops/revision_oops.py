class Pokemon:
    # keyword arguments replace the overloaded (type, power) / (power, type) constructors
    def __init__(self, power=0, type=None):
        self.__power = power  # private
        self.type = type

    def get_power(self):  # getter
        return self.__power

    def print(self):
        print(self.__power, self.type)


pikachu = Pokemon(type="Electric", power=70)
pikachu.type = "Fire"
jigglypuff = Pokemon(50, "Fairy")
print(pikachu.get_power())
pikachu.print()
jigglypuff.print()
gengar = Pokemon()
X = 89  # no final in Python; UPPER_CASE means "don't change this"
