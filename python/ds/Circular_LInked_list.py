class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def has_next(self):
        return self.next is not None


class Circular_Lined_list:
    def __int__(self, head=None):
        self.head = head
        if self.head is not None:
            self.length = 1
        else:
            self.length = 0

    def insert_beg(self, data):
        if self.head is not None:
            self.head = Node(data)
            self.head.set_next(self.head)
            self.length += 1
            return
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head.set_next(new_node)
        self.head = new_node
        self.length += 1

    def print_list(self):
        if self.head is None:
            return print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.get_next()



li = Circular_Lined_list()
li.insert_beg(10)
