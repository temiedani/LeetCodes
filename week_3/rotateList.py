# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # check for empty linkedlist
        if not head or not head.next:
            return head

        # find length of list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # make rotation less than legth
        k = k % length
        if k == 0:
            return head

        # find pivot element
        pivot = head
        for i in range(length-1-k):
            pivot = pivot.next
        # newnode -> ew head of list
        newnode = pivot.next
        # attach pivot to None
        pivot.next = None

        # attach end to beging
        tail.next = head

        return newnode
