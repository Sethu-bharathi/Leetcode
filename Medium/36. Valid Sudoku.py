class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        for row in range(n):
            d1={}
            d2={}
            for col in range(n):
                if board[row][col].isdigit() and board[row][col] in d1:
                    return 0
                else:
                    d1[board[row][col]]=1
                if board[col][row].isdigit() and board[col][row] in d2:
                    return 0
                else:
                    d2[board[col][row]]=1
        for row in range(0,n,3):
            for col in range(0,n,3):
                d1={}
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] in d1:
                            if board[i][j].isdigit():
                                return 0
                        else:
                            d1[board[i][j]]=1
        return 1