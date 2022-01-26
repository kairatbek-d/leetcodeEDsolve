# task:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the
# modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the
# number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Runtime: 52 ms, faster than 68.60%
# Memory Usage: 15.2 MB, less than 44.70%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)

sol = Solution()
ansNode = sol.reverseKGroup(head = node, k = 2)
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next