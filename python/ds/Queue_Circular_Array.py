class Queue:
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def en_queue(self, item):
        if self.size >= self.limit:
            print("Stack Overflow!")
            return

        else:
            self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0

        self.size += 1
        self.rear = self.size - 1
        print("Queue after an en_queue", self.que)

    def de_queue(self):
        if self.size <= 0:
            print("Stack Underflow!")
            return

        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None

            else:
                self.rear = self.size - 1
            print("Queue after de_queue", self.que)

    def queue_front(self):
        if self.front is None:
            print("Queue is empty")
            raise IndexError

        return self.que[self.front]

    def queue_rear(self):
        if self.rear is None:
            print("Queue is empty.")
            raise IndexError
        return self.que[self.rear]

    def size(self):
        return self.size


q = Queue()
q.en_queue(23)
q.en_queue(12)
q.en_queue(99)
q.en_queue(55)
q.en_queue(7)
q.de_queue()
q.queue_front()
q.queue_rear()
