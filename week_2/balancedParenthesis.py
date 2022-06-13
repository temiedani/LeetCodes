from collections import deque
"""
Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]"
"""


def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = deque()
    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if len(stack) == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return len(stack) == 0


print(is_balanced("[{fjdkfj(funnny)dkf}]{}"))
