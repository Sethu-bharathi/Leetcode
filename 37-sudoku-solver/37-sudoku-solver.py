class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row,col,k):
            for i in range(9):
                if board[i][col]==k or board[row][i]==k:
                    return 0
            x=(row//3)*3
            y=(col//3)*3
            for i in range(3):
                for j in range(3):
                    if board[x+i][y+j]==k:
                        return 0
            
            return 1
        
        def dfs(row,col):
            if row==9:
                return 1
            if col==9:
                return dfs(row+1,0)
            if board[row][col]!=".":
                return dfs(row,col+1)
            for i in range(1,10):
                if isValid(row,col,str(i)):
                    board[row][col]=str(i)
                    if dfs(row,col+1):
                        return 1
                    board[row][col]="."
        dfs(0,0)
                    
                    