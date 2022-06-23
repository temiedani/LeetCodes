from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


stack = deque()
# print(dir(stack))

stack.append("lol")
stack.append("you")
stack.append("are")
stack.append("funny")

print(stack)

# reverse a string using a stack


def rev(s: str) -> str:
    st = deque()
    for c in s:
        # push into stack
        st.append(c)
    res = ""
    while len(st) != 0:
        # pop from stack
        res += st.pop()
    return print(res)


rev("temie")
