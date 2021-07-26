class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]    

    def get_stack(self):
        return self.items

def string_reverse(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

stack = Stack()
input_str = "Hello there"

print(string_reverse(stack, input_str))

#print(input_str[::-1])
#random edit