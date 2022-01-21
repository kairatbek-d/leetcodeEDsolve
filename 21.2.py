# task:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the
# nodes of the first two lists.
# Return the head of the merged linked list.


# Runtime: 57 ms, faster than 25.19%
# Memory Usage: 14.3 MB, less than 62.23%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(4)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

sol = Solution()
ansNode = sol.mergeTwoLists(list1=node, list2=node2)
while ansNode is not None:
    print(ansNode.val)
    ansNode = ansNode.next