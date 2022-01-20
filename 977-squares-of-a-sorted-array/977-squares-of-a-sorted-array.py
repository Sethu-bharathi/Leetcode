class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        pos=0
        while A[pos]<0:
            if pos==len(A)-1:
                break
            pos+=1
        neg=pos-1
        if pos==0:
            return [i*i for i in A]
        res=[]
        n=len(A)
        while neg>=0 and pos<n:
            if abs(A[neg])>A[pos]:
                res.append(A[pos]**2)
                pos+=1
            else:
                res.append(A[neg]**2)
                neg-=1
        while neg>=0:
            res.append(A[neg]**2)
            neg-=1
        while pos<n:
            res.append(A[pos]**2)
            pos+=1
        return res
                
        