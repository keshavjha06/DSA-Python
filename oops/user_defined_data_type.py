# classes are blueprints and objects are real world entities
class Student:
    def __init__(self):
        self.name = None
        self.rno = 0
        self.cgpa = 0.0

    def print(self):
        print(self.name, self.rno, self.cgpa)


s1 = Student()
s1.name = "Sam"
s1.rno = 32
s1.cgpa = 1.0

s2 = Student()
s2.name = "Lavish"
s2.rno = 33
s2.cgpa = 2.2

s3 = Student()
s3.name = "Anagha"
s3.rno = int(input())
s3.cgpa = 7.7

print(s1.name, s1.rno, s1.cgpa)
s2.cgpa = 9.7
print(s3.rno)

s1.print()
s2.print()
s3.print()
