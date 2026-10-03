def student_name(a):
    if a % 5 == 0 and a % 3 == 0:
        return "John"
    if a % 3 == 0:
        return "Mary"
    if a % 5 == 0:
        return "Michael"
    return "Keshav"


a = int(input("Enter Number: "))
print(student_name(a))
