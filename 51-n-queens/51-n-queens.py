class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        self.backtrack(board, 0, n, res)
        return res
    
    def backtrack(self, board, row, nq, res):
        if nq == 0:
            res.append(["".join(list) for list in board])
            return 
        
        n = len(board)
        for i in range(n): 
            board[row][i] = "Q"
            if self.isValid(board, row, i):
                self.backtrack(board, row+1, nq-1, res)  
            board[row][i] = "."  
								
    
    def isValid(self, board, i, j):
        n = len(board)
        
        for row in range(i):  
            if board[row][j] == "Q":
                return False
            
        row, col = i, j  
        while 0 <= row < n and 0<= col < n: 
            if board[row][col] == "Q" and (row,col) != (i,j):
                return False
            row,col = row-1, col-1
        
        row, col = i, j
        while 0 <= row < n and 0<= col < n: 
            if board[row][col] == "Q" and (row,col) != (i,j):
                return False
            row,col = row-1, col+1

        return True
            
        