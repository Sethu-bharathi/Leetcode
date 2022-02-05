#User function Template for python3

class Solution:
    def transfigure(self, A, B):
        if len(A)!=len(B):
            return -1
        d={}
        for i in range(len(A)):
            if A[i] in d:
                d[A[i]]+=1
            else:
                d[A[i]]=1
            if B[i] in d:
                d[B[i]]-=1
            else:
                d[B[i]]=-1
        for key in d:
            if d[key]:
                return -1
        count,j=0,len(B)-1
        for i in range(len(A)-1,-1,-1):
            if A[i]==B[j]:
                j-=1
            else:
                count+=1
        return count
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends