class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        p=head
        for i in range(n):
            if temp.next==None:
                if i==n-1:
                    head=head.next
                return head
            temp=temp.next
        while temp.next:
            temp=temp.next
            p=p.next
        p.next=p.next.next
        return head
        