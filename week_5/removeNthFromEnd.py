# LeetCode 19. Remove Nth Node From End of List
'''
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
'''

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    slow = fast = head

    if not head.next:
        return None

    for i in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next if slow.next else None
    return head


def removeNthFromEnd_2(head: ListNode, n: int):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    remove = length-n-1

    if remove < 0:
        return head.next

    cur = head
    while remove > 0:
        cur = cur.next
        remove -= 1

    if not cur.next:
        return None
    elif not cur.next.next:
        cur.next = None
    else:
        cur.next = cur.next.next

    return head