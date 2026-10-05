def greet_except_13():
    for i in range(1, 21):
        print(i)
        if i == 13:
            continue
        print("Good Morning")


greet_except_13()
