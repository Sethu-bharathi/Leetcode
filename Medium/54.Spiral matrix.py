class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top=0
        right=0
        bottom=len(matrix)-1
        left=len(matrix[0])-1
        while top<=bottom and left>=right:
            for i in range(right,left+1):
                res.append(matrix[top][i])
            top+=1
            print(res)
            for i in range(top,bottom+1):
                res.append(matrix[i][left])
            left-=1
            if top<=bottom:
                for i in range(left,right-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            if right<=left:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][right])
                right+=1
            
        return res
        