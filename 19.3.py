# task:
# Given the head of a linked list, remove the nth node from the end of
# the list and return its head.


# Runtime: 51 ms, faster than 23.24%
# Memory Usage: 14 MB, less than 92.21%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

sol = Solution()
ansNode = sol.removeNthFromEnd(head = node, n = 2)
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next