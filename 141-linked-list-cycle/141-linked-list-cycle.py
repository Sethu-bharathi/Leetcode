# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return 0
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return 1
        return 0