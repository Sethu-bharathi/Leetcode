class Solution:
    def compress(self, chars: List[str]) -> int:
        index=1
        count=1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                count+=1
            else:
                if count>1:
                    countstr=str(count)
                    for j in countstr:
                        chars[index]=j
                        index+=1
                count=1
                chars[index]=chars[i]
                index+=1
        if count>1:
            countstr=str(count)
            for j in countstr:
                chars[index]=j
                index+=1
        return index
        