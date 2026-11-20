stack1 = []
print(len(stack1) == 0)  # empty()
stack1.append(34)
stack1.append(3)
stack1.append(54)
stack1.append(32)
stack1.append(7)
print(stack1)
stack1.pop()  # LIFO
print(stack1)
peeked_value = stack1[-1]
print(peeked_value)
print(stack1)
print(54 in stack1)  # contains()
stack1.insert(2, 100)  # insertElementAt(100, 2)
print(stack1)
stack1.pop(0)  # remove(0)
print(stack1)
