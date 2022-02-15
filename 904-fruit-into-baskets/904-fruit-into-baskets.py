class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        maxcount=0
        count=0
        l=0
        r=0
        while r<len(fruits):
            
            if fruits[r] not in d and count==2:
                d[fruits[l]]-=1
                
                if d[fruits[l]]==0:
                    count-=1
                    del d[fruits[l]]
                l+=1
                    
            elif fruits[r] not in d and count<2:
                d[fruits[r]]=1
                count+=1
                r+=1
            elif fruits[r] in d or count<2:
                d[fruits[r]]+=1
                r+=1
            maxcount=max(maxcount,r-l)
        return maxcount    
            