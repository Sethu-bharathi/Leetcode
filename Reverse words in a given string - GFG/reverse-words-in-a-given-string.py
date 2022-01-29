
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        S=S.split(".")
        first=0
        last=len(S)-1
        while first<=last:
            S[first],S[last]=S[last],S[first]
            first+=1
            last-=1
        return ".".join(S)
#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends