# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n=head.val
        while head.next:
            n=(n<<1)|head.next.val
            head=head.next
        return n