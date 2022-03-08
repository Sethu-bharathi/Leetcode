
class Solution:
    def __init__(self):
        self.res=[]
    def combinations(self,n,index,arr,k):
        if len(arr)==k:
            self.res.append(arr)
            return 
        for i in range(index,n+1):
            self.combinations(n,i+1,arr+[i],k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations(n,1,[],k)
        return (self.res)
        