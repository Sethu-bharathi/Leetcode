class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line=0
        pixel=0
        for i in s:
            pixel+=widths[ord(i)-ord("a")]
            
            if pixel>100:
                line+=1
                pixel=widths[ord(i)-ord("a")]
        if pixel==0:
            return [line,0]
        return [line+1,pixel]
        