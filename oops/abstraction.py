# Abstraction = hiding implementation details and showing only essential features.
# Python uses the abc module for abstract classes.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):  # abstract method (no body)
        pass

    def fuel_type(self):  # concrete method
        print("Petrol/Diesel")


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


v = Car()
v.start()
v.fuel_type()
