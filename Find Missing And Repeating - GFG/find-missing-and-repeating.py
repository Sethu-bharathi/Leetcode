#User function Template for python3

class Solution:
    def findTwoElement(self,nums, n): 
        s=0
        for j,i in enumerate(nums):
            if nums[abs(i)-1]<0:
                res=abs(i)
            else:
                nums[abs(i)-1]*=-1
            s+=abs(i)
        
        s1=(n*(n+1))>>1
        s-=res
        return[s1-s,res][::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends