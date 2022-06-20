#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        if n==1:
            return [1]
        res=[i for i in nums]
        l=len(nums)
        for i in range(1,len(nums)):
            nums[i]*=nums[i-1]
            temp=l-i
            res[temp-1]*=res[temp]
        temp=[0]*l
        for i in range(1,l-1):
            temp[i]=res[i+1]*nums[i-1]
        temp[0]=res[1]
        temp[-1]=nums[-2]
        return temp
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends