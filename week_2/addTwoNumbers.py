# LeetCode No 2. Add Two Numbers

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # def reverse(self,head):
    #     prev=None
    #     current=head
    #     while current:
    #         nextNode=current.next
    #         current.next=prev
    #         prev=current
    #         current=nextNode
    #     return prev
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        current_node = result
        carry = 0

        while l1 or l2 or carry > 0:
            # get values
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # calculate sum
            sum = (v1+v2+carry) % 10

            # update carry
            carry = (v1+v2+carry)//10

            # carry, sum = divmod(val1+val2 + carry, 10)

            # create new node
            new_node = ListNode(sum)
            current_node.next = new_node
            current_node = current_node.next

            # update to next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
