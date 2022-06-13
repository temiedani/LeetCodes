from collections import deque
stack = deque()
print(dir(stack))

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
