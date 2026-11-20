class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class InsertNode:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, "--> ", end="")
            current = current.next
        print("None")

    def insert_first(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, position, value):
        # 1 -> 4 -> 5
        # 1 -> 6 -> 4 -> 5
        node = ListNode(value)
        if position == 1:
            node.next = self.head
            self.head = node
            return

        previous = self.head
        count = 1
        while count < position - 1:
            previous = previous.next
            count += 1
        current = previous.next
        node.next = current
        previous.next = node

    def insert_last(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node


sll = InsertNode()
sll.insert(1, 3)  # 3 -> None
sll.insert(2, 5)  # 3 -> 5 -> None
sll.insert(1, 2)  # 2 -> 3 -> 5 -> None
sll.insert(2, 4)  # 2 -> 4 -> 3 -> 5 -> None
sll.insert(5, 7)  # 2 -> 4 -> 3 -> 5 -> 7 -> None
sll.display()
