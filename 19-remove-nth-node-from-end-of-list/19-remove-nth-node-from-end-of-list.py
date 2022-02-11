# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr=head
        prev=head
        for i in range(n):
            if curr.next==None:
                if i==n-1:
                    head=head.next
                return head
            curr=curr.next
        while curr and curr.next:
            prev=prev.next
            curr=curr.next
        if prev.next:
            prev.next=prev.next.next
        else:
            prev.next=None
        return head
        
        