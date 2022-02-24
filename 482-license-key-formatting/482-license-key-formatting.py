class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res=""
        for i in s:
            if i!="-":
                res+=i.upper()
        i=len(res)
        r=i%k
        res1=[]
        if r!=0:
            res1.append(res[:r])
        i=r
        
        for i in range(r,len(res),k):
            res1.append(res[i:i+k])
        return "-".join(res1)
        
                