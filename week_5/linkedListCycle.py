# LeetCode 141. Linked List Cycle
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list 
that can be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''
# Linear solution


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    current = head
    visited = {}
    while current:
        if current.next in visited:
            return True
        visited[current.next] = "visited"
        current = current.next
    return False

# Logarthmic Solution


def hasCycle_2(head):
    if not head or not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
