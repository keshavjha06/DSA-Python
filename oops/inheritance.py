# Method overloading: Python has no overloading, so a default
# argument lets one method handle 2 or 3 numbers.
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


c = Calculator()
print(c.add(2, 3))  # 5
print(c.add(2, 3, 4))  # 9
print(c.add(2.5, 3.5))  # 6.0
