# task:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the
# modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the
# number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Runtime: 66 ms, faster than 38.75%
# Memory Usage: 15.3 MB, less than 44.70%

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, curr = 0, head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k: return head   # list shorter than k
        new_head, prev = self.reverseList(head, k)
        head.next = self.reverseKGroup(new_head, k)   # the size-k reversed list produced by self.reverseList(head, k) reads: prev -> ... -> head
        return prev

    def reverseList(self, head: ListNode, count: int) -> ListNode:
        prev = ListNode(None)
        curr = head
        while count > 0:
            next_node = curr.next   # break curr -> curr.next
            curr.next = prev   # reverse to prev <- curr
            prev = curr   # increment prev node
            curr = next_node   # increment curr node
            count -= 1
        return (curr, prev)   # prev is the head node of the reversed list, the end node of the original list
                              # curr is the head node of the remaining list, since it is the node following prev in the original list

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