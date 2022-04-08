class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[0])
        final_end_date=max(j for i,j in events)
        li,ptr,attended=[],0,0
        heapq.heapify(li)
        for curr_day in range(1,final_end_date+1):
            while ptr<len(events) and events[ptr][0]==curr_day:
                heapq.heappush(li,events[ptr][1])
                ptr+=1
            while li and li[0]<curr_day:
                heapq.heappop(li)
            if li:
                heapq.heappop(li)
                attended+=1
        return attended
                