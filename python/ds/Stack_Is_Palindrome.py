class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def is_Palindrome(string):
    stack = Stack()
    for char in string:
        stack.push(char)

    for char in string:
        if char != stack.pop():
            print("String is not Palindrome.")
            return False

    print("String is Palindrome.")
    return True


print(is_Palindrome("aannaa"))
