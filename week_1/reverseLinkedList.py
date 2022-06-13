# Definition for singly-linked list.
from contextlib import nullcontext


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # Itertive method
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous
    # recursive method

    def reverseList_2(self, head: ListNode) -> ListNode:
        return head
