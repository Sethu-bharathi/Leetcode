#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        res=""
        flag=0
        for i in S:
            if i==".":
                if res and res[-1]==".":
                    res+="0"
                flag=0
                res+=i
            elif i!="0" or flag:
                res+=i
                flag=1
        if res[0]==".":
            res="0"+res
        if res and res[-1]==".":
                res+="0"
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends