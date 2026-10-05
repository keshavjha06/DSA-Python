def do_while_demo():
    # Python has no do-while; "while True" + break runs the body at least once
    i = 11
    while True:
        print(i)
        i += 1
        if i > 10:
            break


def while_demo():
    i = 1
    while i <= 10:
        print(i)
        i += 1


do_while_demo()
while_demo()
