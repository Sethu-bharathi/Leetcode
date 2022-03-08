class Solution:
    def __init__(self):
        self.res=[]
    def sumn(self,arr,index,k,n,sum1):
        if len(arr)==k and sum1==n:
            self.res.append(arr)
            return
        if len(arr)>k or sum1>n:
            return
        for i in range(index,10):
            self.sumn(arr+[i],i+1,k,n,sum1+i)
            
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.sumn([],1,k,n,0)
        return(self.res)