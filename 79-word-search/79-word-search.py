class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C=len(board),len(board[0])
        fn=len
        def dfs(i,j,index):
            temp=board[i][j]
            if index==fn(word)-1 and word[index]==board[i][j]:
                return 1
            elif word[index]==board[i][j]:
                temp,board[i][j]=board[i][j],"*"
                if i>=1:
                    if dfs(i-1,j,index+1):
                        return 1
                if i<R-1:
                    if dfs(i+1,j,index+1):
                        return 1
                if j>=1:
                    if dfs(i,j-1,index+1):
                        return 1
                if j<C-1:
                    if dfs(i,j+1,index+1):
                        return 1
            board[i][j]=temp
            return 0
        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False