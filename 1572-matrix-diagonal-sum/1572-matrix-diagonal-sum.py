class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        j=0
        n=len(mat)-1
        for i in range(len(mat)):
            if j!=n-j:
                sum+=mat[i][j]+mat[i][n-j]
            else:
                sum+=mat[i][j]
            j+=1
        return sum