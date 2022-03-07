class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def dfs(i,j):
            count=0
            x,y=i,j
            while i<8:
                if board[i][j]=="p":
                    count+=1
                    break
                elif board[i][j]=="B":
                    break
                i+=1
            i=x
            while i>=0:
                if board[i][j]=="p":
                    count+=1
                    break
                elif board[i][j]=="B":
                    break
                i-=1
            i=x
            while j<8:
                if board[i][j]=="p":
                    count+=1
                    break
                elif board[i][j]=="B":
                    break
                j+=1
            j=y
            while j>=0:
                if board[i][j]=="p":
                    return count+1
                elif board[i][j]=="B":
                    return count
                j-=1
            return count
        for i in range(8):
            for j in range(8):
                if board[i][j]=="R":
                       return dfs(i,j)