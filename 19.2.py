# task:
# Given the head of a linked list, remove the nth node from the end of
# the list and return its head.


# Runtime: 56 ms, faster than 16.09%
# Memory Usage: 14.3 MB, less than 49.43%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]

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