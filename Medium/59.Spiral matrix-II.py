class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for i in range(n)] for i in range(n)]
        top=0
        right=0
        bottom=len(matrix)-1
        left=len(matrix[0])-1
        index=1
        while top<=bottom and left>=right:
            for i in range(right,left+1):
                matrix[top][i]=index
                index+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][left]=index
                index+=1
            left-=1
            if top<=bottom:
                for i in range(left,right-1,-1):
                    matrix[bottom][i]=index
                    index+=1
                bottom-=1
            if right<=left:
                for i in range(bottom,top-1,-1):
                    matrix[i][right]=index
                    index+=1
                right+=1
            
        return matrix