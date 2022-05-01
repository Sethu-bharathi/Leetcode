class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d={}
        mindist=float("inf")
        for i in range(len(cards)):
            if cards[i] in d:
                mindist=min(mindist,i-d[cards[i]]+1)
                d[cards[i]]=i
            else:
                d[cards[i]]=i
        if mindist==float("inf"):
            return -1
        return mindist
                
                    
            