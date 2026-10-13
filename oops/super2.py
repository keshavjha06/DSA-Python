# Call the parent's version of an overridden method with super()
class Parents:
    def show(self):
        print("Parent method")


class Childs(Parents):
    def show(self):
        print("Child method")

    def display(self):
        self.show()  # child method
        super().show()  # parent method


c = Childs()
c.display()
