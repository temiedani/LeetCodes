
# Leetcode 20. Valid Parentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

from collections import deque


def balanced_2(sentence: str) -> bool:
    stack = deque()
    valid = {'}': '{', ']': '[', ')': '('}
    for s in sentence:
        if s == ')' or s == ']' or s == '}':
            if len(stack) == 0:
                return False
            elif stack.pop() != valid[s]:
                return False
        elif s == '(' or s == '[' or s == '{':
            stack.append(s)
    return len(stack) == 0


print(balanced_2("[{fjdkfj(funnny)dkf}]{}"))
