class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        fn=ord
        x=fn(t[0])
        for i in t[1:]:
            x^=fn(i)
        for i in s:
            x^=fn(i)
        return (chr(x))
str1=input()
str2=input()
diff=Solution()
print(diff.findTheDifference(str1,str2))