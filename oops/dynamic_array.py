class DynamicArray:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.index = 0
        self.size = 0

    def add(self, ele):
        if self.index == len(self.arr):  # array is full
            self.capacity_increase()
        self.arr[self.index] = ele
        self.index += 1
        self.size += 1

    def remove_from_end(self):
        self.index -= 1
        self.size -= 1

    def capacity(self):
        return len(self.arr)

    def capacity_increase(self):
        new_arr = [0] * (len(self.arr) * 2)
        for i in range(len(self.arr)):  # copy old elements
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def get(self, index):
        return self.arr[index]

    def set(self, index, val):
        self.arr[index] = val

    def display(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


arr = DynamicArray(8)
arr.add(10)
arr.add(20)
arr.add(30)
arr.display()
print(arr.get(1))
arr.add(40)
arr.add(40)
arr.add(40)
arr.add(40)
arr.add(40)
arr.add(40)
arr.display()
