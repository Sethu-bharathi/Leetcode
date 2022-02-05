# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[(node.val,i) for i,node in enumerate(lists) if node]
        head=ListNode(0)
        curr=head
        heapq.heapify(heap)
        while heap:
            _,index=heapq.heappop(heap)
            node=lists[index]
            curr.next=node
            curr=curr.next
            if node.next:
                lists[index]=node.next
                heapq.heappush(heap,(node.next.val,index))
        return head.next
            
        