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


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2

    elif op == "/":
        return op1 / op2

    elif op == "+":
        return op1 + op2

    else:
        return op1 - op2


def postfix_cal(postfixExpr):
    operand = Stack()
    string = postfixExpr.split()
    for token in string:
        if token in "0123456789":
            operand.push(int(token))
        else:
            operand2 = operand.pop()
            operand1 = operand.pop()
            result = doMath(token, operand1, operand2)
            operand.push(result)
    return operand.pop()

print(postfix_cal("1 2 3 * + 5 -"))