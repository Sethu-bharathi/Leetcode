class Solution:
    def swap(self,matrix,i,j,x,y) -> None:
        matrix[i][j],matrix[x][y]=matrix[x][y],matrix[i][j]
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                self.swap(matrix,i,j,j,i)
        for i in range(n):
            for j in range(n//2):
                self.swap(matrix,i,j,i,-(j+1))
        return matrix
        
        
        