# Access parent class variable with super() when the child uses the same name
class Parent:
    x = 10


class Child(Parent):
    x = 20

    def show(self):
        print("Child x:", self.x)
        print("Parent x:", super().x)


c = Child()
c.show()
