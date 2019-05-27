# https://leetcode.com/problems/add-two-numbers/
#
# Program takes in two linked lists representing two reversed non-negative integers and
# returns the sum, also reversed, in linked-list format.
#
# Runtime: 68 ms, faster than 99.20% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.3 MB, less than 33.03% of Python3 online submissions for Add Two Numbers.
# (5/26/2019)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        head = current = ListNode(0)
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, value = divmod(carry, 10)
            current.next = current = ListNode(value)
        
        return head.next
