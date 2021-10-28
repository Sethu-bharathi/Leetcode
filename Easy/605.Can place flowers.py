class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev=0
        for i in flowerbed:
            if prev==0 and i==0:
                n-=1
                prev=1
                continue
            elif prev==1 and i==1:
                n+=1
            prev=i
        return n<=0
        