class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            tmp = [0]*26
            for c in s:
                tmp[ord(c)-ord('a')]+=1
            tmp = tuple(tmp)
            if tmp in result:
                result[tmp].append(s)
            else:
                result[tmp] = [s]
        
        return result.values()