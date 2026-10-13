# Call the parent constructor with super().__init__()
class Parentss:
    def __init__(self):
        print("Parent constructor")


class Childss(Parentss):
    def __init__(self):
        super().__init__()
        print("Child constructor")


c = Childss()
