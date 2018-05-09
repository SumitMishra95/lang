class DynamicArrayStack:
    def __init__(self, maxsize=None):
        self.stack = []
        self.maxsize = maxsize
        self.length = 0

    def __del__(self):
        return self.clear()

    def clear(self):
        self.stack = []
        self.length = 0

    def push(self, data):
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception("Stack is full.")
        self.stack.append(data)
        print("Stack after push", self.stack)
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is Empty.")
        temp = self.stack[-1]
        self.stack.remove(self.stack[-1])
        self.length -= 1

        print("Element popped ", temp)
        print("Stack after push", self.stack)

    def top(self):
        print(self.stack[-1])

    def size(self):
        print(self.length)

    def isEmpty(self):
        print(self.stack == 0)

    def IsFull(self):
        print(self.stack == self.maxsize)


st = DynamicArrayStack()
st.push(11)
st.push(22)
st.push(33)
st.push(44)
st.IsFull()
st.pop()
st.top()
st.size()