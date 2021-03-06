# task:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


# Runtime: 214 ms, faster than 20.06%
# Memory Usage: 18 MB, less than 55.27%

# Definition for singly-linked list.
from queue import PriorityQueue
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next

node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

sol = Solution()
ansNode = sol.mergeKLists([node, node2, node3])
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next