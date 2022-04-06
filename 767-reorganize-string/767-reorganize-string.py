class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s)==1:
            return s
        d=collections.Counter(s)
        heap=[]
        n=len(s)
        for i in d:
            if d[i]>(n//2+n%2):
                return ""
            heapq.heappush(heap,[-d[i],i])
        s=""
        curr=heapq.heappop(heap)
        while heap:
            s+=curr[1]
            print(s,curr,heap)
            curr[0]+=1
            prev=curr
            curr=heapq.heappop(heap)
            if prev[0]!=0:
                heapq.heappush(heap,prev)
        if curr[0]:
            return s+curr[1]
        return s
            