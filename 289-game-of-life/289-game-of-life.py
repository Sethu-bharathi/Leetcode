class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        R,C=len(board),len(board[0])
        def countones(i,j):
            x=[0,0,-1,-1,-1,1,1,1]
            y=[-1,1,-1,0,1,-1,0,1]
            count=0
            for a,b in zip(x,y):
                if 0<=i+a<R and 0<=j+b<C and board[i+a][j+b]:
                    count+=1
            return count
        updated=[[countones(j,i) for i in range(C)] for j in range(R)]
        for i in range(R):
            for j in range(C):
                temp=updated[i][j]
                if (board[i][j] and temp==2) or temp==3:
                    board[i][j]=1
                else:
                    board[i][j]=0
                    
                
            
        