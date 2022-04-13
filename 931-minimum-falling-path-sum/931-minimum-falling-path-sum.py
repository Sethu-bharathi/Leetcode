class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r,c=len(matrix),len(matrix[0])
        dy=[-1,0,1]
        for i in range(1,r):
            for j in range(c):
                ans=float("inf")
                for k in dy:
                    x=i-1
                    y=j-k
                    if 0<=x<r and 0<=y<c:
                        ans=min(ans,matrix[x][y])
                matrix[i][j]+=ans
        ans=float("inf")
        for j in range(c):
            ans=min(ans,matrix[r-1][j])
        return ans
                