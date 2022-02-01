class Solution:
    def minimumTotal(self, A) -> int:
        row = A[-1]
        for i in reversed( range(len(A)-1) ):
            row = [ x + min(row[j],row[j+1]) for j,x in enumerate(A[i]) ]
        return row[0]
        