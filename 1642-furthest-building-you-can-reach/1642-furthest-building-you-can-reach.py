class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev=math.inf
        heap=[]
        for i in range(len(heights)-1):
            if heights[i]>=heights[i+1]:
                continue
            temp=heights[i+1]-heights[i]
            heapq.heappush(heap,-temp)
            if bricks-temp<0:
                if ladders:
                    curr=-heapq.heappop(heap)
                    ladders-=1
                    bricks+=curr
                else:
                    return i
            bricks-=temp
        return i+1
            