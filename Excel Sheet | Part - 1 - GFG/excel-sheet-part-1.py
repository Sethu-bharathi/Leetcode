#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        s=""
        char=[chr(i+ord('A')) for i in range(26)]
        while N>0:
            N,res=divmod(N-1,26)
            s=char[res]+s
        return s
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends