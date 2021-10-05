class Solution:
    def reverseString(self, s: list[str]) -> None:
        start,end=0,len(s)-1
        while start<end:
            s[start],s[end]=s[end],s[start]
            end-=1
            start+=1
reverse=Solution()
string=[i for i in input()]
reverse.reverseString(string)
print(string)