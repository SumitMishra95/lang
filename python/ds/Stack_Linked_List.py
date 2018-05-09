class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def has_next(self):
        return self.next is not None


class LinkedListStack:
    def __init__(self, maxsize=None, head=None):
        self.maxsize = maxsize
        self.head = head
        if self.head is not None:
            self.length = 1
        else:
            self.length = 0

    def __str__(self):
        current = self.head
        aux = []
        while current is not None:
            aux.append(current.get_data())
            current = current.get_next()
        return print(str(aux))

    def clear(self):
        self.head = None
        self.length = 0

    def push(self, data):
        if self.maxsize is not None and self.length + 1 >= self.maxsize:
            raise Exception("Stack is Full.")

        if self.head is None:
            self.head = Node(data)
            self.__str__()
            self.length += 1
            return

        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp
        self.__str__()
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is empty")
        temp = self.head
        self.head = self.head.get_next()
        self.length -= 1
        print("After popping ", temp.get_data())
        self.__str__()

    def top(self):
        return print(self.head)

    def size(self):
        return print(self.length)

    def is_empty(self):
        return print(self.length == 0)


s = LinkedListStack()
s.push(11)
s.push(22)
s.push(33)
s.pop()
