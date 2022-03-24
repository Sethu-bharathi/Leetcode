class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        first,last=0,len(people)-1
        res=0
        while first<last:
            if people[first]+people[last]<=limit:
                res+=1
                first+=1
                last-=1
            else:
                res+=1
                last-=1
        if first==last:
            return res+1
        return res