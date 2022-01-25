# task:
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the
# problem without modifying the values in the list's nodes (i.e., only nodes themselves may
# be changed.)


# Runtime: 28 ms, faster than 90.16%
# Memory Usage: 14.3 MB, less than 16.33%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

sol = Solution()
ansNode = sol.swapPairs(node)
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next