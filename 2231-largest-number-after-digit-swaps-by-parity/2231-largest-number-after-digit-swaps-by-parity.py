class Solution:
    def largestInteger(self, num: int) -> int:
        odd,even=[],[]
        arr=list(map(int,str(num)))
        for i in arr:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        odd,even=sorted(odd),sorted(even)
        res=0
        for i in arr:
            if i%2:
                res=res*10+odd.pop()
            else:
                res=res*10+even.pop()
        return res