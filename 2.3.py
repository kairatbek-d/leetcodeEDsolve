# task:
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as
# a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в
# обратном порядке, и каждый из их узлов содержит одну цифру. Сложите два числа и верните сумму в виде
# связанного списка.
# Вы можете предположить, что эти два числа не содержат нуля в начале, кроме самого числа 0.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 59ms and 96.34%
class Solution:
    BASE = 10
    DEFAULT_VALUE = 0
    DEFAULT_NEXT = None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result_dummy_head = ListNode()       # Dummy node just for appending nodes later
        curr1, curr2, curr_result = l1, l2, result_dummy_head
        
        while curr1 != None or curr2 != None or carry != 0:
            addition = carry + getattr(curr1, 'val', self.DEFAULT_VALUE) + getattr(curr2, 'val', self.DEFAULT_VALUE)
            carry, result_value = divmod(addition, self.BASE)
            curr_result.next = ListNode(result_value)
            
            curr1 = getattr(curr1, 'next', self.DEFAULT_NEXT)
            curr2 = getattr(curr2, 'next', self.DEFAULT_NEXT)
            curr_result = curr_result.next

        return result_dummy_head.next


sol = Solution()

node1 = ListNode(3)
node1.next = ListNode(5)
node1.next.next = ListNode(7)

node2 = ListNode(2)
node2.next = ListNode(6)
node2.next.next = ListNode(3)

ansNode = sol.addTwoNumbers(l1 = node1, l2 = node2)

while ansNode is not None:
    print(ansNode.val)

    ansNode = ansNode.next