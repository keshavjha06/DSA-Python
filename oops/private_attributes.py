class Students:
    def __init__(self):
        self.name = None
        self.__rno = 0  # double underscore = private (name mangled)
        self.cgpa = 0.0

    def print(self):
        print(self.name, self.__rno, self.cgpa)

    def get_rno(self):  # getter
        return self.__rno

    def set_rno(self, x):  # setter
        self.__rno = x


s = Students()
s.print()
s.name = "Jack"
s.cgpa = 8.9
# s.__rno -> AttributeError outside the class
s.set_rno(45)
print(s.get_rno())

sb = input()
print(sb)  # prints the same given input
