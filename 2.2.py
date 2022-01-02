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

# 121ms and 5.25%
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        head = ListNode(-1)
        node = head
        spillOver = False
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next 
            if l2:
                val += l2.val
                l2 = l2.next

            if spillOver:
                val += 1
            
            if val >= 10:
                val -= 10
                spillOver = True
            else:
                spillOver = False
            
            node.next = ListNode(val)
            node = node.next
        
        if spillOver:
            node.next = ListNode(1)

        return head.next

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