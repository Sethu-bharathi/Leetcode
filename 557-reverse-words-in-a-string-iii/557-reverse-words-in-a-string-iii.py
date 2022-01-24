class Solution(object):
    def reverseWords(self, s):
        s=" ".join(s.split(" ")[::-1])
        s=s[::-1]
        return s
                
        
        
        