class StudentData:
    def __init__(self, data):
        self.name = None
        self.rno = 0
        if isinstance(data, int):
            self.marks = [0] * data  # empty marks of given size
        else:
            # self.marks = data would share the same list (output -> 40)
            self.marks = data.copy()


arr = [4, 1, 7, 3, 5]
s1 = StudentData(arr)
s1.marks[0] = 40
print(arr[0])
s2 = StudentData(2)
