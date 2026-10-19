def search(stack, item):
    # 1-based position from the top, or -1 if not found
    position = 1
    for i in range(len(stack) - 1, -1, -1):
        if stack[i] == item:
            return position
        position += 1
    return -1


st = []
st.append(10)  # push
st.append(20)
st.append(30)
st.append(40)
print(st)  # [10, 20, 30, 40]
st.pop()
print(st)  # [10, 20, 30]
print(st[-1])  # 30 (peek)
print(search(st, 50))  # -1
print(len(st) == 0)  # False
st.clear()
print(len(st) == 0)  # True
