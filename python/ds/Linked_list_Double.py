class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def has_prev(self):
        return self.prev is not None


class Double_linked_list:
    def __init__(self, Node=None):
        self.head = self.tail = Node
        if self.head == 0:
            self.length = 0
        else:
            self.length = 1

    def insert_beg(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
            self.length += 1
            return

        new_node = Node(data)
        self.head.set_prev(new_node)
        new_node.set_next(self.head)
        self.head = new_node
        self.length += 1

    def insert_end(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
            self.length += 1
            return

        new_node = Node(data)
        self.tail.set_next(new_node)
        new_node.set_prev(self.tail)
        self.tail = new_node
        self.length += 1

    def insert_pos(self, pos, data):
        if pos > self.length or pos < 0:
            raise IndexError("Index Error.")
        if pos == 0:
            self.insert_beg(data)
            return

        elif pos == self.length:
            self.insert_end(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0
        while count < pos:
            current = current.get_next()
            count += 1
        new_node.set_next(current)
        new_node.set_prev(current.get_prev())
        current.get_prev().set_next(new_node)
        current.set_prev(new_node)
        self.length += 1

    def delete_beg(self):
        if self.length == 0:
            raise IndexError("List is Empty.")

        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return

        self.head.get_next().set_prev(None)
        self.head = self.head.get_next()
        self.length -= 1

    def delete_end(self):
        if self.length == 0:
            raise IndexError("List is Empty.")

        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return

        self.tail.get_prev().set_next(None)
        self.tail = self.tail.get_prev()
        self.length -= 1

    def delete_pos(self, pos):
        if self.length == 0:
            raise IndexError("List is empty.")

        if pos > self.length or pos < 0:
            raise IndexError("Index doesn't Error")

        if pos == 0:
            self.delete_beg()
            return

        if pos == self.length - 1:
            self.delete_end()
            return

        current = self.head
        count = 0
        while count < pos:
            current = current.get_next()
            count += 1

        current.get_prev().set_next(current.get_next())
        current.get_next().set_prev(current.get_prev())
        self.length -= 1

    def delete_node(self, node):
        if self.length == 0:
            raise IndexError("List is empty")

        else:
            previous = None
            current = self.head
            if self.head == node:
                self.delete_beg()
                return

            if self.tail == node:
                self.delete_end()
                return

            found = False
            while current.get_next() is not None and found == False:
                previous = current
                current = current.get_next()
                if current == node:
                    found = True

            if not found:
                raise IndexError("Node not found.")

            previous.set_next(current.get_next())
            current.get_next().set_prev(previous)
            self.length -= 1

    def print_list(self):
        if self.head is None:
            return print("List is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.get_next()


li = Double_linked_list()
li.insert_beg(10)
li.insert_end(20)
li.insert_pos(1, 15)
li.delete_node(10)
li.print_list()
