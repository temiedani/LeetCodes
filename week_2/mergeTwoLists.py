# 21. Merge Two Sorted Lists
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        current_node = result

        while l1 and l2:

            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next

            current_node.next = new_node
            current_node = current_node.next

        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2

        return result.next

    def mergeTwoLists_2(self, head1, head2):

        temp = None
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head1.val <= head2.val:
            temp = head1
            temp.next = self.mergeTwoLists_2(head1.next, head2)
        else:
            temp = head2
            temp.next = self.mergeTwoLists_2(head1, head2.next)
        return temp
