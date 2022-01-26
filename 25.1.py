# task:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the
# modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the
# number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Runtime: 82 ms, faster than 21.15%
# Memory Usage: 15 MB, less than 93.33%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next

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