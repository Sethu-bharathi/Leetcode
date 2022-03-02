class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index=-1
        dist=float("inf")
        for j,i in enumerate(points):
            if i[0]==x or i[1]==y:
                t=(abs(x-i[0])+abs(y-i[1]))
                if t<dist:
                    dist=t
                    index=j
        return index