class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        s=[[1],[1,1]]
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return s
        else:
            for i in range(1,numRows-1):
                ans=[1]
                for j in range(len(s[i])-1):
                    ans.append(s[i][j]+s[i][j+1])
                ans.append(1)
                s.append(ans)
        return s