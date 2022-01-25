# task:
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the
# problem without modifying the values in the list's nodes (i.e., only nodes themselves may
# be changed.)


# Runtime: 46 ms, faster than 29.51%
# Memory Usage: 14.2 MB, less than 77.71%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode(0)
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            p.next = tmp
            head = head.next
            p = tmp.next
        return dummy.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

sol = Solution()
ansNode = sol.swapPairs(node)
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next