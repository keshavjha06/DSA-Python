def print_even_with_check():
    # loop runs 100 times
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def print_even_with_step():
    # loop runs 50 times
    for i in range(2, 101, 2):
        print(i, end=" ")
    print()


print_even_with_check()
print_even_with_step()
