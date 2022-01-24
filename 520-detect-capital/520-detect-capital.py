class Solution(object):
    def detectCapitalUse(self, word):
        if len(word)>1:
            if word[0].isupper() and word[1].islower():
                for i in range(2,len(word)):
                    if word[i].isupper():
                        return 0
                return 1
        upper=0
        lower=0
        for i in range(len(word)):
            if word[i].isupper():
                upper=1
                if lower:
                    return 0
            elif word[i].islower():
                lower=1
                if upper:
                    return 0
        return 1
                
            
            
        