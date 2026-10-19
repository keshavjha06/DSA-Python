from collections import deque

queue = deque()
queue.append(10)  # offer
queue.append(20)
queue.append(30)
queue.append(40)
print(list(queue))  # [10, 20, 30, 40]
print(queue.popleft())  # 10 (poll)
print(list(queue))  # [20, 30, 40]
print(queue[0])  # 20 (peek)
print(len(queue) == 0)  # False
queue.clear()
print(len(queue) == 0)  # True

print("--------------------------------")

dq = deque()
dq.append(10)
dq.appendleft(20)  # offerFirst
dq.appendleft(30)
dq.appendleft(40)
print(list(dq))  # [40, 30, 20, 10]
print(dq.popleft())  # 40 (pollFirst)
print(list(dq))  # [30, 20, 10]
print(dq.pop())  # 10 (pollLast)
print(list(dq))  # [30, 20]
print(dq[0])  # 30 (peekFirst)
print(dq[-1])  # 20 (peekLast)
print(list(dq))
print(len(dq) == 0)  # False
dq.clear()
print(len(dq) == 0)  # True
