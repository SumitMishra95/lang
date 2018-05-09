class Dynamic_Array_Stack:
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
        return self.stack == 0

    def IsFull(self):
        print(self.stack == self.maxsize)


def check_symbol_balance(input):
    symbol_stack = Dynamic_Array_Stack()
    balanced = 0

    for symbol in input:
        if symbol in ["(", "{", "["]:
            symbol_stack.push(symbol)

        else:
            if symbol_stack.isEmpty():
                balanced = 0
                if symbol in [")", "}", "]"]:
                    return print("Not balanced.")

            else:
                top = symbol_stack.pop()
                if (top == "(" and symbol == ")") or (top == "[" and symbol == "]") or (top == "{" and symbol == "}"):
                    balanced = 1

                else:
                    balanced = 0
    return print(bool(balanced))

check_symbol_balance("()")
