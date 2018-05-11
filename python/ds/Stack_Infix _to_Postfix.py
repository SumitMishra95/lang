class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def top(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def infix_to_postfix(string):
    operands = Stack()
    result = []
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    tokens = string.split()
    for symbol in tokens:
        if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or symbol in "1234567890":
            result.append(symbol)
        elif symbol in "(":
            operands.push(symbol)
        elif symbol in ")":
            top = operands.pop()
            while top != "(":
                result.append(top)
                top = operands.pop()
        else:
            while not operands.is_empty() and prec[operands.top()] >= prec[symbol]:
                result.append(operands.pop())
            operands.push(symbol)

    while not operands.is_empty():
        result.append(operands.pop())
    return " ".join(result)


print(infix_to_postfix("A / B - C * D + E"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
