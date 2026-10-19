from collections import deque

ll = deque()
ll.append(40)
ll.append(50)
ll.append(60)
ll.appendleft(10)  # addFirst
ll.append(20)  # addLast
ll.insert(1, 30)
print(list(ll))  # [10, 30, 40, 50, 60, 20]
ll.popleft()  # removeFirst
ll.pop()  # removeLast
print(list(ll))  # [30, 40, 50, 60]

print(ll[0])  # 30 (first)
print(ll[-1])  # 60 (last)

print(ll[0])  # 30 (peek)
print(list(ll))
print(ll.popleft())  # 30 (poll)
print(list(ll))  # [40, 50, 60]
ll.append(100)  # offer
print(list(ll))  # [40, 50, 60, 100]
