class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,left=0,len(matrix[0])-1
        
        while top<len(matrix) and left>=0:
            if matrix[top][left]==target:return 1
            elif matrix[top][left]>target:
                left-=1
            else:
                top+=1
        return 0