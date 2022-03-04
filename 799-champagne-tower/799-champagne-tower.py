class Solution:
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        arr=[[0]*k for k in range(1,102)]
        arr[0][0]=poured
        for i in range(query_row+1):
            for j in range(i+1):
                x=(arr[i][j]-1.0)/2.0
                if x>0:
                    arr[i+1][j]+=x
                    arr[i+1][j+1]+=x
        return min(1,arr[query_row][query_glass])
        