class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[0 for i in range(n+1)]
        for i in range(1,n+1):
            arr[i]=arr[(i&(i-1))]+1
        return arr