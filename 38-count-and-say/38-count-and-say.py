class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return("1")
        num="1"
        for i in range(n-1):
            count=1
            nextnum=""
            for i in range(1,len(num)):
                if num[i]==num[i-1]:
                    count+=1
                else:
                    nextnum+=str(count)+str(num[i-1])
                    count=1
            nextnum+=str(count)+str(num[-1])
            num=nextnum
            n-=1
        return nextnum