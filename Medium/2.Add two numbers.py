# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=num2=0
        ten=1
        temp=l1
        while(temp):
            num1+=temp.val*ten
            ten*=10
            temp=temp.next
        temp=l2
        ten=1
        while(temp):
            num2+=temp.val*ten
            ten*=10
            temp=temp.next
        num1+=num2
        head=ListNode()
        temp=head
        while 1:
            temp.val=num1%10
            num1//=10
            if num1>0:
                temp.next=ListNode()
                temp=temp.next
            else:
                return head
            
        
        
        
        