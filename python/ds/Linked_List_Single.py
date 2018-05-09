class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None


class SingleLinked:

    def __init__(self, head=None):
        self.head = head
        if self.head is not None:
            self.length = 1
        else:
            self.length = 0

    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    # Insert at the beginning of the list
    def insert_beg(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    # Insert at the end of the list
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.length += 1

    # Insert at any position of the list
    def insert_pos(self, pos, data):
        if pos > self.length or pos < 0:
            raise IndexError("Index is not correct")
        else:
            if pos == 0:
                self.insert_beg(data)
            elif pos == self.length:
                self.insert_end(data)
            else:
                new_node = Node(data)
                count = 0
                current = self.head
                while count < pos:
                    current = current.get_next()
                    count += 1
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1

    # Delete from the beginning of the list
    def delete_beg(self):
        if self.length == 0:
            raise IndexError("List is already empty.")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    # Delete from the end of the list
    def delete_end(self):
        if self.length == 0:
            raise IndexError("List is already empty.")
        else:
            current = self.head
            previous = self.head
            while current.get_next is not None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            self.length -= 1

    # Delete from any position from the list
    def delete_pos(self, pos):
        if self.length == 0:
            raise IndexError("List is already empty.")

        if self.length < pos or pos < 0:
            raise IndexError("Index out of bound.")

        else:
            if pos == 0:
                self.delete_beg()
            elif pos == self.length - 1:
                self.delete_end()
            else:
                current = self.head
                previous = None
                count = 0
                while count < pos:
                    previous = current
                    current = current.get_next()
                    count += 1
                previous.set_next(current.get_next())
                self.length -= 1

    # Delete any specific value from list
    def delete_value(self, value):
        if self.length == 0:
            raise IndexError("List has no elements to delete.")
        else:
            previous = None
            current = self.head
            if current.get_data() == value:
                self.delete_beg()
                return
            found = False
            while current.get_next() is not None and found == False:
                previous = current
                current = current.get_next()
                if current.get_data() == value:
                    found = True

            if found == False:
                raise Exception("Node not found.")

            previous.set_next(current.get_next())
            self.length -= 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.get_next()


li = SingleLinked()
li.insert_beg(35)
li.insert_beg(25)
li.insert_beg(15)
li.insert_beg(5)
li.insert_end(45)
li.insert_pos(2, 30)
li.insert_pos(2, 28)
li.delete_beg()
li.delete_pos(2)
li.delete_value(30)
li.print_list()
