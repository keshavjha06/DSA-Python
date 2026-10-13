# Python has no interface keyword; an ABC with only abstract methods plays that role.
from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def sound(self):
        pass


class Cat(Animals):
    def sound(self):
        print("Cat Meows")


a = Cat()
a.sound()
