class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("Stack overflow!")

        else:
            self.stk.append(item)
            print("Stack after push", self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")

        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Stack Underflow!")

        else:
            print(self.stk[::-1])

    def size(self):
        print(len(self.stk))


st = Stack(5)
st.push(11)
st.push(22)
st.push(33)
st.push(44)
st.push(55)
st.push(66)
st.peek()
st.pop()
st.peek()
st.size()
