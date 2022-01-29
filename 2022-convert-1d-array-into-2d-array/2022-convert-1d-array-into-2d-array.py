class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            print(m*n,len(original))
            return []
        res=[]
        index=0
        for i in range(m):
            res.append([])
            for j in range(n):
                res[-1].append(original[index])
                index+=1
            
        return res
        