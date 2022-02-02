#User function Template for python3
from math import log
class Solution:
    def findPosition(self, n):
        if n&(n-1) or n<1:
            return -1
        if(n>0):
            return int(log(n,2))+1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends