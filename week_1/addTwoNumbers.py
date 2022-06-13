# Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


from numpy import integer


def addTwoNumbers(l1, l2):
    l1.reverse(), l2.reverse()
    s1 = [str(integer) for integer in l1]
    a_string = "".join(s1)
    l11 = int(a_string)
    s2 = [str(integer) for integer in l2]
    a_string = "".join(s2)
    l22 = int(a_string)
    res = str(l11+l22)
    return list(res[::-1])


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
