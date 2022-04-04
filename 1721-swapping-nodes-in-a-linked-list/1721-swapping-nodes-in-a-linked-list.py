# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end=head
        start=head
        for i in range(k-1):
            if end==None:
                return head
            end=end.next
        temp=end
        while end.next:
            start=start.next
            end=end.next
        start.val,temp.val=temp.val,start.val
        return head
        