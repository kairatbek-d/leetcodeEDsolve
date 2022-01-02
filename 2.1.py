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

# 149ms and 5.09%
class Solution:
    def summing(self,val1=0,val2=0):
        sumval = (val1+val2)
        rem = 0
        if sumval/10>=1.0:
            return sumval%10,sumval//10
        return sumval,rem

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem=0
        head=temp=ListNode(0)
        while l1 or l2:
            if l1 and l2:
                sumval,rem = self.summing(l1.val,l2.val+rem)
                l1,l2 = l1.next,l2.next
            elif l1:
                sumval,rem=self.summing(l1.val+rem)
                l1 = l1.next
            else:
                sumval,rem=self.summing(l2.val+rem)
                l2 = l2.next
            temp.next = ListNode(sumval)
            temp = temp.next
        if rem:
            temp.next= ListNode(rem)
        return head.next



sol = Solution()

node1 = node3 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)

ansNode = sol.addTwoNumbers(l1 = node1, l2 = node2)

while ansNode is not None:
    print(ansNode.val)

    ansNode = ansNode.next

# while node3 is not None:
#     print(node3.val) # 2 4 3

#     node3 = node3.next